import logging
import dash
from src.apps import home, aboutme, individual, company, contact, impressum, company
from dash import dcc, ctx
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from src.apps.utils.dash_base_template import DashBasePage
import logging.config
from src.app import app, server
import os
from flask import send_from_directory, request, jsonify
import psycopg
from psycopg.rows import dict_row
from datetime import datetime
import resend
from dotenv import load_dotenv
import sqlite3

load_dotenv()

# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
text = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black", "font-size": "20px"}
SAVE_THE_DATE_PASSWORD = os.environ.get("SAVE_THE_DATE_PASSWORD", "150826")
SAVE_THE_DATE_FAMILY_PASSWORD = os.environ.get("SAVE_THE_DATE_FAMILY_PASSWORD", "140826")
DATABASE_URL = os.environ.get("DATABASE_URL")
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
LOCAL_DB_PATH = os.environ.get("LOCAL_DB_PATH", "local_rsvp.db")
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "thams.florian@gmail.com")
# RSVP can have multiple recipients (comma-separated)
RSVP_EMAILS = [e.strip() for e in os.environ.get("RSVP_EMAILS", "thams.florian@gmail.com").split(",")]

# Database type flag
USE_POSTGRES = bool(DATABASE_URL)

# Invitation page constants
INVITATION_FROM_ADDRESS = "RSVP Hochzeit <onboarding@resend.dev>"
ALLOWED_DIETS = {"Ich esse alles", "Vegetarisch", "Vegan"}


def get_db_connection():
    """Get a database connection (PostgreSQL or SQLite)."""
    if USE_POSTGRES:
        return psycopg.connect(DATABASE_URL, row_factory=dict_row, connect_timeout=5)
    else:
        conn = sqlite3.connect(LOCAL_DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn


def get_all_rsvps():
    """Get all RSVP entries from the database."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT guest_name, attending FROM rsvp ORDER BY guest_name')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        # Convert to list of dicts
        return [{'name': row['guest_name'], 'attending': bool(row['attending'])} for row in rows]
    except Exception as e:
        logger.error(f"Error fetching RSVPs: {e}")
        return []


def _save_guests_to_db(guests, table, extra_columns_per_guest, submitted_at=None):
    """Insert one row per guest into `table`. Returns submission_group UUID string.

    extra_columns_per_guest(guest_dict) -> dict of additional column-name -> value.
    `guest_name`, `submitted_at`, `submission_group` are always written.
    `submitted_at` defaults to datetime.now() if not provided; pass an explicit
    value when the caller needs the same timestamp for downstream side effects
    (e.g. email body) so the DB row and email agree.
    """
    import uuid
    submission_id = str(uuid.uuid4())
    if submitted_at is None:
        submitted_at = datetime.now()

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        for guest in guests:
            extras = extra_columns_per_guest(guest) or {}
            columns = ['guest_name'] + list(extras.keys()) + ['submitted_at', 'submission_group']
            if USE_POSTGRES:
                placeholders = ', '.join(['%s'] * len(columns))
                values = [guest['name']] + list(extras.values()) + [submitted_at, submission_id]
            else:
                placeholders = ', '.join(['?'] * len(columns))
                # Coerce booleans to 0/1 for SQLite
                coerced = []
                for v in extras.values():
                    if isinstance(v, bool):
                        coerced.append(1 if v else 0)
                    else:
                        coerced.append(v)
                values = [guest['name']] + coerced + [submitted_at.isoformat(), submission_id]
            sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
            cur.execute(sql, values)
        conn.commit()
    finally:
        cur.close()
        conn.close()
    return submission_id


def _send_rsvp_email(subject, body, from_address):
    """Send an RSVP summary email via Resend. Returns True on success, False on failure."""
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY not configured, skipping email notification")
        return False
    try:
        resend.api_key = RESEND_API_KEY
        resend.Emails.send({
            "from": from_address,
            "to": RSVP_EMAILS,
            "subject": subject,
            "text": body,
        })
        return True
    except Exception as e:
        logger.error(f"Email error: {e}")
        return False


def init_db():
    """Initialize the database tables if they don't exist."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        if USE_POSTGRES:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS rsvp (
                    id SERIAL PRIMARY KEY,
                    guest_name VARCHAR(255) NOT NULL,
                    attending BOOLEAN NOT NULL,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    submission_group UUID NOT NULL
                )
            ''')
        else:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS rsvp (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guest_name TEXT NOT NULL,
                    attending INTEGER NOT NULL,
                    submitted_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    submission_group TEXT NOT NULL
                )
            ''')
        if USE_POSTGRES:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS invitation_rsvp (
                    id SERIAL PRIMARY KEY,
                    guest_name VARCHAR(255) NOT NULL,
                    diet VARCHAR(50) NOT NULL,
                    allergies TEXT NOT NULL DEFAULT '',
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    submission_group UUID NOT NULL
                )
            ''')
        else:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS invitation_rsvp (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guest_name TEXT NOT NULL,
                    diet TEXT NOT NULL,
                    allergies TEXT NOT NULL DEFAULT '',
                    submitted_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    submission_group TEXT NOT NULL
                )
            ''')
        conn.commit()
        cur.close()
        conn.close()
        db_type = "PostgreSQL" if USE_POSTGRES else f"SQLite ({LOCAL_DB_PATH})"
        logger.info(f"Database initialized successfully: {db_type}")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")


class Navigation(DashBasePage):

    def __init__(self):
        super().__init__()
        self.path = ""
        self.app.callback(Output("page-content", "children"), [Input("url", "pathname")])(self.display_page)

        self.app.callback(
            Output(f"navbar-collapse2", "is_open"),
            [Input(f"navbar-toggler2", "n_clicks")],
            [State(f"navbar-collapse2", "is_open")],
        )(self.toggle_navbar_collapse)

        self.app.callback(
            [
                Output(f"timeline", "active"),
                Output(f"info1", "is_open"),
                Output(f"info2", "is_open"),
                Output(f"info3", "is_open"),
                Output(f"time1", "children"),
                Output(f"time2", "children"),
                Output(f"time3", "children"),
            ],
            [
                Input(f"time1", "n_clicks"),
                Input(f"time2", "n_clicks"),
                Input(f"time3", "n_clicks"),
            ],
            [
                State(f"info1", "is_open"),
                State(f"info2", "is_open"),
                State(f"info3", "is_open"),
            ],
        )(self.timeline_toggler)

        self.app.callback(
            [
                Output("alert-dismiss", "hide"),
                Output("alert-dismiss_error", "hide"),
                Output("submit-button", "disabled"),
            ],
            [
                Input("submit-button", "n_clicks"),
                Input("firstname", "value"),
                Input("lastname", "value"),
                Input("email", "value"),
                Input("text", "value"),
            ],
            [
                State("alert-dismiss", "hide"),
                State("alert-dismiss_error", "hide"),
                State("submit-button", "disabled"),
            ],
            prevent_initial_call=True,
        )(self.send_formular)

        self.register_callbacks(self.app)
        logging.info(dash.callback_context)

    def layout(self):
        return dbc.Container(
            children=[
                html.Div(
                    [
                        dbc.Row(
                            [
                                dmc.Title(
                                    f"Veränderungen annehmen, angehen und gestalten.".upper(),
                                    order=2,
                                    color="white",
                                    align="center",
                                    weight=0,
                                    style={
                                        "background": "#25274D",  # "#A1AAA5",
                                        "font-family": headline["font-family"],
                                        "font-weight": "normal",
                                    },
                                )
                            ]
                        ),
                        dcc.Location(id="url", refresh=False),
                        dbc.Row(
                            dbc.Col(
                                [
                                    dbc.Navbar(
                                        dbc.Container(
                                            [
                                                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                                                dbc.Collapse(
                                                    dbc.Nav(
                                                        self.navitems(),
                                                        # justified=True,
                                                        fill=True,
                                                        pills=True,
                                                        # navbar=True,
                                                        # vertical="lg",
                                                        horizontal="center",
                                                        # className="d-flex justify-content-center",
                                                        # navbar_scroll=True,
                                                    ),
                                                    id="navbar-collapse2",
                                                    navbar=True,
                                                    # className="d-flex justify-content-around",
                                                    # dimension="width",
                                                    style={
                                                        "align": "center",
                                                        "background-color": "white",
                                                        "justify-content": "center",
                                                    },
                                                ),
                                            ],
                                        ),
                                        expand="md",
                                        # light=True,
                                        color="white",
                                        # className="d-flex justify-content-center",
                                        style={
                                            "align": "center",
                                            "background-color": "white",
                                            "justify-content": "center",
                                        },
                                    ),
                                ],
                                width={"size": 10},
                                align="center",
                            ),
                            justify="center",
                            style={
                                "margin-bottom": "0px",
                            },
                        ),
                    ],
                ),
                html.Div(id="page-content"),
            ],
            fluid=True,
        )

    def navitems(self):
        return [
            dbc.NavItem(
                dbc.NavLink(
                    "Home",
                    href="/home",
                    style=headline,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Über mich",
                    href="/aboutme",
                    style=headline,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Privatperson",
                    href="/individual",
                    style=headline,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Führungskraft/UnternehmerIn",
                    href="/company",
                    style=headline,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Kontakt",
                    href="/contact",
                    style=headline,
                )
            ),
        ]

    def display_page(self, pathname):
        print(pathname)
        print(f" {dash.callback_context.inputs}")
        if pathname == "/home":
            return home.layout
        if pathname == "/aboutme":
            return aboutme.layout
        if pathname == "/individual":
            return individual.layout
        if pathname == "/company":
            print(f"company.layout: {company.layout}")
            return company.layout
        if pathname == "/contact":
            print(f"contact.layout: {contact.layout}")
            return contact.layout
        if pathname == "/impressum":
            return impressum.layout
        return home.layout

    def toggle_navbar_collapse(self, n, is_open):
        button_clicked = ctx.triggered_id
        print("navbar_toggler")
        print(f"button_clicked: {button_clicked}")
        print(f" {dash.callback_context.args_grouping}")
        print(f" {dash.callback_context.inputs}")
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
        if "navbar-toggler2" in changed_id:
            return not is_open
        return is_open

    def timeline_toggler(self, button1, button2, button3, time1, time2, time3):
        print("timeline_toggler")
        triggered_prop_ids = ctx.triggered_prop_ids
        print(f"triggered_prop_ids: {triggered_prop_ids}")
        print(f" {dash.callback_context.args_grouping}")
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
        print(f"changed_id: {changed_id}")
        if "time1" in changed_id:
            time1 = not time1
        elif "time2" in changed_id:
            time2 = not time2
        elif "time3" in changed_id:
            time3 = not time3
        if time3:
            active = 3
        elif time2:
            active = 2
        elif time1:
            active = 1
        else:
            active = 0

        return (
            active,
            time1,
            time2,
            time3,
            self.determine_button_name(time1),
            self.determine_button_name(time2),
            self.determine_button_name(time3),
        )

    def determine_button_name(self, state):
        if state:
            return "Hide"
        return "Show more"

    def send_formular(self, submit, firstname, lastname, email, text, hide_successful, hide_error, disabled):
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
        print(f"changed_id: {changed_id}")
        print(f"text: {text}")
        print(f"hide_successful: {hide_successful}")
        print(f"hide_error: {hide_error}")
        print(f"firstname: {firstname}")
        print(f"lastname: {lastname}")
        print(f"email: {email}")
        if "submit" in changed_id:
            if not RESEND_API_KEY:
                print("RESEND_API_KEY not configured")
                return hide_successful, not hide_error, disabled

            try:
                resend.api_key = RESEND_API_KEY
                resend.Emails.send({
                    "from": "kontakt@beas-coaching.de",
                    "to": NOTIFICATION_EMAIL,
                    "subject": f"Kontaktformular beas-coaching.de - {firstname} {lastname}",
                    "text": f"Von: {firstname} {lastname}\nE-Mail: {email}\n\nNachricht:\n{text}"
                })
                return not hide_successful, hide_error, True
            except Exception as e:
                print(e)
                return hide_successful, not hide_error, disabled
        elif (email is not None) and ("@" in email) and (text is not None):
            return hide_successful, hide_error, False
        return hide_successful, hide_error, disabled


page = Navigation()
page.app.layout = page.layout
server = page.app.server


# Hidden Save the Date page routes
SAVE_THE_DATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'assets', 'save-the-date')


@server.route('/save-the-date')
def save_the_date():
    return send_from_directory(SAVE_THE_DATE_DIR, 'index.html')


@server.route('/save-the-date/<path:filename>')
def save_the_date_assets(filename):
    return send_from_directory(SAVE_THE_DATE_DIR, filename)


@server.route('/save-the-date/verify', methods=['POST'])
def save_the_date_verify():
    data = request.get_json()
    if data and data.get('password') == SAVE_THE_DATE_PASSWORD:
        return jsonify({'success': True})
    return jsonify({'success': False}), 401


def _save_the_date_handler(from_address):
    """Shared handler body for save-the-date and save-the-date-family RSVP routes."""
    data = request.get_json()
    if not data or 'guests' not in data:
        return jsonify({'success': False, 'error': 'No guest data provided'}), 400

    guests = data['guests']
    if not guests:
        return jsonify({'success': False, 'error': 'No guests in submission'}), 400

    submitted_at = datetime.now()

    try:
        _save_guests_to_db(
            guests,
            'rsvp',
            lambda g: {'attending': g['attending']},
            submitted_at=submitted_at,
        )
    except Exception as e:
        logger.error(f"Database error: {e}")
        return jsonify({'success': False, 'error': 'Database error'}), 500

    # Email is best-effort; only build it when we'll actually send.
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY not configured, skipping email notification")
        return jsonify({'success': True})

    # Build email content for new submission (preserved character-for-character)
    new_guest_list = "\n".join([
        f"  - {g['name']}: {'Kommt' if g['attending'] else 'Kommt nicht'}"
        for g in guests
    ])
    new_attending_count = sum(1 for g in guests if g['attending'])

    all_rsvps = get_all_rsvps()
    total_attending = sum(1 for g in all_rsvps if g['attending'])
    total_not_attending = sum(1 for g in all_rsvps if not g['attending'])

    attending_list = "\n".join([
        f"  - {g['name']}"
        for g in all_rsvps if g['attending']
    ]) or "  (noch keine)"

    not_attending_list = "\n".join([
        f"  - {g['name']}"
        for g in all_rsvps if not g['attending']
    ]) or "  (noch keine)"

    email_text = f"""Neue RSVP-Anmeldung für die Hochzeit!

Datum: {submitted_at.strftime('%d.%m.%Y %H:%M')}

Neue Anmeldung:
{new_guest_list}

Zusagen (neu): {new_attending_count} von {len(guests)}

════════════════════════════════════════
GESAMTÜBERSICHT
════════════════════════════════════════

ZUSAGEN ({total_attending}):
{attending_list}

ABSAGEN ({total_not_attending}):
{not_attending_list}

GESAMT: {len(all_rsvps)} Rückmeldungen ({total_attending} Zusagen, {total_not_attending} Absagen)

---
Diese E-Mail wurde automatisch generiert.
"""
    subject = f"RSVP Hochzeit - {new_attending_count} neue Zusage(n) | Gesamt: {total_attending} Zusagen"
    _send_rsvp_email(subject, email_text, from_address)
    return jsonify({'success': True})


@server.route('/save-the-date/rsvp', methods=['POST'])
def save_the_date_rsvp():
    """Handle RSVP submissions - save to database and send email notification."""
    return _save_the_date_handler("kontakt@beas-coaching.de")


# Hidden Save the Date Family page routes
SAVE_THE_DATE_FAMILY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'assets', 'save-the-date-family')


@server.route('/save-the-date-family')
def save_the_date_family():
    return send_from_directory(SAVE_THE_DATE_FAMILY_DIR, 'index.html')


@server.route('/save-the-date-family/<path:filename>')
def save_the_date_family_assets(filename):
    return send_from_directory(SAVE_THE_DATE_FAMILY_DIR, filename)


@server.route('/save-the-date-family/verify', methods=['POST'])
def save_the_date_family_verify():
    data = request.get_json()
    if data and data.get('password') == SAVE_THE_DATE_FAMILY_PASSWORD:
        return jsonify({'success': True})
    return jsonify({'success': False}), 401


@server.route('/save-the-date-family/rsvp', methods=['POST'])
def save_the_date_family_rsvp():
    """Handle RSVP submissions - save to database and send email notification."""
    return _save_the_date_handler("RSVP Hochzeit <onboarding@resend.dev>")


# Hidden Invitation page routes
INVITATION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'assets', 'invitation')


@server.route('/invitation')
def invitation_page():
    return send_from_directory(INVITATION_DIR, 'index.html')


@server.route('/invitation/verify', methods=['POST'])
def invitation_verify():
    data = request.get_json(silent=True)
    if data and data.get('password') == SAVE_THE_DATE_PASSWORD:
        return jsonify({'success': True})
    return jsonify({'success': False}), 401


@server.route('/invitation/rsvp', methods=['POST'])
def invitation_rsvp():
    """Handle invitation RSVP submissions - save to database and send email."""
    data = request.get_json(silent=True)
    if not data or 'guests' not in data:
        return jsonify({'success': False, 'error': 'No guest data provided'}), 400

    guests = data['guests']
    if not guests:
        return jsonify({'success': False, 'error': 'No guests in submission'}), 400

    # Validate every guest before any insert
    normalized = []
    for g in guests:
        name = (g.get('name') or '').strip()
        if not name:
            return jsonify({'success': False, 'error': 'Empty guest name'}), 400
        diet = g.get('diet')
        if diet not in ALLOWED_DIETS:
            return jsonify({'success': False, 'error': 'Invalid diet'}), 400
        allergies = g.get('allergies') or ''
        normalized.append({'name': name, 'diet': diet, 'allergies': allergies})

    submitted_at = datetime.now()
    try:
        _save_guests_to_db(
            normalized,
            'invitation_rsvp',
            lambda g: {'diet': g['diet'], 'allergies': g['allergies']},
            submitted_at=submitted_at,
        )
    except Exception as e:
        logger.error(f"Database error: {e}")
        return jsonify({'success': False, 'error': 'Database error'}), 500

    # Email is best-effort; only build it when we'll actually send.
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY not configured, skipping email notification")
        return jsonify({'success': True})

    try:
        # New submission lines
        new_lines = "\n".join([
            f"  - {g['name']} ({g['diet']}) | Allergien: {g['allergies'] if g['allergies'] else '—'}"
            for g in normalized
        ])

        # Pull complete summary
        all_rows = _get_all_invitation_rsvps()
        diet_counts = {"Ich esse alles": 0, "Vegetarisch": 0, "Vegan": 0}
        for row in all_rows:
            if row['diet'] in diet_counts:
                diet_counts[row['diet']] += 1

        all_guest_lines = "\n".join([
            f"  - {row['guest_name']} ({row['diet']})"
            for row in all_rows
        ]) or "  (noch keine)"

        allergy_lines = "\n".join([
            f"  - {row['guest_name']}: {row['allergies']}"
            for row in all_rows if row['allergies']
        ]) or "  (keine Allergien gemeldet)"

        new_count = len(normalized)
        total_count = len(all_rows)
        subject = (
            f"Einladung RSVP - {new_count} neue Anmeldung(en) | "
            f"Allesesser: {diet_counts['Ich esse alles']} | "
            f"Veg: {diet_counts['Vegetarisch']} | "
            f"Vegan: {diet_counts['Vegan']}"
        )
        body = f"""Neue Einladungs-RSVP für die Hochzeit!

Datum: {submitted_at.strftime('%d.%m.%Y %H:%M')}

Neue Anmeldung:
{new_lines}

════════════════════════════════════════
GESAMTÜBERSICHT
════════════════════════════════════════

ERNÄHRUNG:
  Allesesser:    {diet_counts['Ich esse alles']}
  Vegetarisch:   {diet_counts['Vegetarisch']}
  Vegan:         {diet_counts['Vegan']}
  GESAMT:        {total_count} Gäste

ALLERGIEN & UNVERTRÄGLICHKEITEN:
{allergy_lines}

ALLE GÄSTE ({total_count}):
{all_guest_lines}

---
Diese E-Mail wurde automatisch generiert.
"""
        _send_rsvp_email(subject, body, "kontakt@beas-coaching.de")
    except Exception as e:
        logger.error(f"Invitation email build error: {e}")

    return jsonify({'success': True})


@server.route('/invitation/<path:filename>')
def invitation_assets(filename):
    return send_from_directory(INVITATION_DIR, filename)


def _get_all_invitation_rsvps():
    """Return all invitation_rsvp rows as list of dicts."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT guest_name, diet, allergies FROM invitation_rsvp ORDER BY guest_name')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [
            {'guest_name': r['guest_name'], 'diet': r['diet'], 'allergies': r['allergies']}
            for r in rows
        ]
    except Exception as e:
        logger.error(f"Error fetching invitation RSVPs: {e}")
        return []


# Initialize database on startup
init_db()


if __name__ == "__main__":
    page.app.run_server(port=8000, host="0.0.0.0", debug=True)
