import logging
from src.apps import home, aboutme, individual, company, contact
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
font_definition = {"font-family": "Georgia", "color": "black"}


class Navigation(DashBasePage):

    def __init__(self):
        super().__init__()
        self.path = ""
        self.app.callback(Output("page-content", "children"), [Input("url", "pathname")])(self.display_page)

        for i in [2]:
            self.app.callback(
                Output(f"navbar-collapse{i}", "is_open"),
                [Input(f"navbar-toggler{i}", "n_clicks")],
                [State(f"navbar-collapse{i}", "is_open")],
            )(self.toggle_navbar_collapse)

    def layout(self):
        return dbc.Container(
            children=[
                html.Div(
                    [
                        dbc.Row(
                            [
                                dmc.Title(
                                    f"Veränderungen annehmen, angehen und gestalten.",
                                    order=2,
                                    color="white",
                                    align="center",
                                    weight=0,
                                    style={"background": "#A1AAA5", "font-family": "Georgia", "font-weight": "normal"},
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
                                                    className="d-flex justify-content-around",
                                                    # dimension="width",
                                                ),
                                            ],
                                        ),
                                        expand="md",
                                        # light=True,
                                        color="white",
                                        # className="d-flex justify-content-center",
                                        # style={"align": "center", "background-color": "white"},
                                    ),
                                ],
                                width={"size": 10},
                                align="center",
                            ),
                            justify="center",
                        ),
                        dmc.Divider(variant="solid"),
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
                    style=font_definition,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Über mich",
                    href="/aboutme",
                    style=font_definition,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Privatperson",
                    href="/individual",
                    style=font_definition,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Führungskraft/Unternehmer",
                    href="/company",
                    style=font_definition,
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Kontakt",
                    href="/contact",
                    style=font_definition,
                )
            ),
        ]

    def display_page(self, pathname):
        print(pathname)
        if pathname == "/home":
            return home.layout
        if pathname == "/aboutme":
            print("True")
            return aboutme.layout
        if pathname == "/individual":
            return individual.layout
        if pathname == "/company":
            return company.layout
        if pathname == "/contact":
            return contact.layout
        return home.layout

    def toggle_navbar_collapse(self, n, is_open):
        if n:
            return not is_open
        return is_open


page = Navigation()
page.app.layout = page.layout
server = page.app.server

if __name__ == "__main__":
    page.app.run_server(port=8000, host="0.0.0.0", debug=True)


# D6DCE5
