import logging
from src.apps import home, aboutme, individual, company, contact
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src.apps.utils.dash_base_template import DashBasePage
import logging.config
from src.app import app, server

# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
font_definition = {"font-family": "Georgia"}


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
                        dcc.Location(id="url", refresh=False),
                        dbc.NavbarSimple(
                            [
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
                            ],
                            brand="",
                            color="lightgray",
                            dark=False,
                        ),
                    ],
                ),
                html.Div(id="page-content"),
            ],
            fluid=True,
        )

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
