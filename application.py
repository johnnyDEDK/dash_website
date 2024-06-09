import logging
import dash
from src.apps import home, aboutme, individual, company, contact, impressum
from dash import dcc, ctx
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from src.apps.utils.dash_base_template import DashBasePage
import logging.config
from src.app import app, server
import smtplib
from email.mime.text import MIMEText
import os


# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
text = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black", "font-size": "20px"}
SMTP_SERVER = os.environ.get("smtp_server")
SMTP_LOGIN = os.environ.get("smtp_login")
SMTP_PW = os.environ.get("smtp_pw")


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
                                        "background": "#A1AAA5",
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
                    "Führungskraft/Unternehmer",
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
            # Configuration
            port = 465
            sender_email = "web454@ebeas-coaching.de"
            receiver_email = "beatrice_koch@gmx.de"

            # Plain text content
            # Create MIMEText object
            message = MIMEText(text, "plain")
            message["Subject"] = f"Kontaktformular beas-coaching.de - Send from: {firstname} {lastname}: {email}"
            message["From"] = sender_email
            message["To"] = receiver_email

            # Send the email
            try:
                with smtplib.SMTP_SSL(SMTP_SERVER, port) as server:
                    server.login(SMTP_LOGIN, SMTP_PW)
                    server.sendmail(sender_email, receiver_email, message.as_string())

                return not hide_successful, hide_error, True
            except:
                return hide_successful, not hide_error, disabled
        elif (email is not None) and ("@" in email) and (text is not None):
            return hide_successful, hide_error, False
        return hide_successful, hide_error, disabled


page = Navigation()
page.app.layout = page.layout
server = page.app.server

if __name__ == "__main__":
    page.app.run_server(port=8000, host="0.0.0.0", debug=True)
