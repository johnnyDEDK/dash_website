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


def get_db_connection():
    """Get a database connection (PostgreSQL or SQLite)."""
    if USE_POSTGRES:
        return psycopg.connect(DATABASE_URL, row_factory=dict_row)
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
                    "from": "Kontaktformular <onboarding@resend.dev>",
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


@server.route('/save-the-date/rsvp', methods=['POST'])
def save_the_date_rsvp():
    """Handle RSVP submissions - save to database and send email notification."""
    import uuid

    data = request.get_json()
    if not data or 'guests' not in data:
        return jsonify({'success': False, 'error': 'No guest data provided'}), 400

    guests = data['guests']
    if not guests:
        return jsonify({'success': False, 'error': 'No guests in submission'}), 400

    submission_id = str(uuid.uuid4())
    submitted_at = datetime.now()

    # Save to database
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        for guest in guests:
            if USE_POSTGRES:
                cur.execute(
                    'INSERT INTO rsvp (guest_name, attending, submitted_at, submission_group) VALUES (%s, %s, %s, %s)',
                    (guest['name'], guest['attending'], submitted_at, submission_id)
                )
            else:
                cur.execute(
                    'INSERT INTO rsvp (guest_name, attending, submitted_at, submission_group) VALUES (?, ?, ?, ?)',
                    (guest['name'], 1 if guest['attending'] else 0, submitted_at.isoformat(), submission_id)
                )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"Database error: {e}")
        return jsonify({'success': False, 'error': 'Database error'}), 500

    # Send email notification via Resend
    if RESEND_API_KEY:
        try:
            resend.api_key = RESEND_API_KEY

            # Build email content for new submission
            new_guest_list = "\n".join([
                f"  - {g['name']}: {'Kommt' if g['attending'] else 'Kommt nicht'}"
                for g in guests
            ])
            new_attending_count = sum(1 for g in guests if g['attending'])

            # Get complete RSVP summary from database
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

            resend.Emails.send({
                "from": "RSVP Hochzeit <onboarding@resend.dev>",
                "to": RSVP_EMAILS,
                "subject": f"RSVP Hochzeit - {new_attending_count} neue Zusage(n) | Gesamt: {total_attending} Zusagen",
                "text": email_text
            })

        except Exception as e:
            logger.error(f"Email error: {e}")
            # Don't fail the request if email fails, data is already saved
    else:
        logger.warning("RESEND_API_KEY not configured, skipping email notification")

    return jsonify({'success': True})


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
    import uuid

    data = request.get_json()
    if not data or 'guests' not in data:
        return jsonify({'success': False, 'error': 'No guest data provided'}), 400

    guests = data['guests']
    if not guests:
        return jsonify({'success': False, 'error': 'No guests in submission'}), 400

    submission_id = str(uuid.uuid4())
    submitted_at = datetime.now()

    # Save to database
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        for guest in guests:
            if USE_POSTGRES:
                cur.execute(
                    'INSERT INTO rsvp (guest_name, attending, submitted_at, submission_group) VALUES (%s, %s, %s, %s)',
                    (guest['name'], guest['attending'], submitted_at, submission_id)
                )
            else:
                cur.execute(
                    'INSERT INTO rsvp (guest_name, attending, submitted_at, submission_group) VALUES (?, ?, ?, ?)',
                    (guest['name'], 1 if guest['attending'] else 0, submitted_at.isoformat(), submission_id)
                )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"Database error: {e}")
        return jsonify({'success': False, 'error': 'Database error'}), 500

    # Send email notification via Resend
    if RESEND_API_KEY:
        try:
            resend.api_key = RESEND_API_KEY

            # Build email content for new submission
            new_guest_list = "\n".join([
                f"  - {g['name']}: {'Kommt' if g['attending'] else 'Kommt nicht'}"
                for g in guests
            ])
            new_attending_count = sum(1 for g in guests if g['attending'])

            # Get complete RSVP summary from database
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

            resend.Emails.send({
                "from": "RSVP Hochzeit <onboarding@resend.dev>",
                "to": RSVP_EMAILS,
                "subject": f"RSVP Hochzeit - {new_attending_count} neue Zusage(n) | Gesamt: {total_attending} Zusagen",
                "text": email_text
            })

        except Exception as e:
            logger.error(f"Email error: {e}")
            # Don't fail the request if email fails, data is already saved
    else:
        logger.warning("RESEND_API_KEY not configured, skipping email notification")

    return jsonify({'success': True})


# Initialize database on startup
init_db()


if __name__ == "__main__":
    page.app.run_server(port=8000, host="0.0.0.0", debug=True)
