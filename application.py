import logging
import dash
from requests import head
from src.apps import home, aboutme, individual, company, contact, references
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from src.apps.utils.dash_base_template import DashBasePage
import logging.config
from src.app import app, server

# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
text = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black", "font-size": "20px"}


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
            Output(f"timeline", "active"),
            [
                Input(f"info1", "aria-expanded"),
                Input(f"info2", "is_open"),
                Input(f"info3", "is_open"),
            ],
        )(self.timeline_toggler)
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
            return company.layout
        if pathname == "/contact":
            return contact.layout
        if pathname == "/references":
            return references.layout
        return home.layout

    def toggle_navbar_collapse(self, n, is_open):
        print("navbar_toggler")
        print(f" {dash.callback_context.args_grouping}")
        print(f" {dash.callback_context.inputs}")
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
        if "navbar-toggler2" in changed_id:
            return not is_open
        return is_open

    def timeline_toggler(self, info1, info2, info3):
        print("timeline_toggler")
        print(f" {dash.callback_context.args_grouping}")
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered]
        print(f"changed_id: {changed_id}")
        active = 0
        if "info1" in changed_id:
            active = 1
        elif "info2" in changed_id:
            active = 2
        elif "info3" in changed_id:
            active = 3
        return active


page = Navigation()
page.app.layout = page.layout
server = page.app.server

if __name__ == "__main__":
    page.app.run_server(port=8000, host="0.0.0.0", debug=True)


# D6DCE5
