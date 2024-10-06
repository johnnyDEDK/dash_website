import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..ui.layout import FrontEndLayout

from dash import dcc
from dash import html

import logging
import os


logger = logging.getLogger(__name__)
card_color = "#edf1fa"  # "#EDEBE7"
accordion_color = card_color  # "-#D6DCE5"  # "#F8F9FA"
textfont = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black"}


class Contact(FrontEndLayout):
    def __init__(self, **kwargs):
        logger.debug("Start init Layout.__init__()")
        super().__init__()
        logger.debug("End init Layout.__init__()")

    def layout(self):
        return html.Div([self._layout_body()])

    def _layout_body(self):
        return dmc.MantineProvider(
            theme={
                "fontFamily": textfont["font-family"],
                "primaryColor": "dark",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            },
            children=[
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._layout_body_card(),
                                    width={"size": 10},
                                    md={"size": 10},
                                    sm={"size": 10},
                                    lg={"size": 10},
                                    xl={"size": 8},  # , "offset": 1},
                                    xxl={"size": 6},  # , "offset": 1},
                                    style={
                                        "align-self": "center",
                                        "background-color": card_color,
                                        "justify-content": "center",
                                    },
                                    align="center",
                                    class_name="g-0",
                                ),
                            ],
                            class_name="g-0",
                            align="center",
                            style={
                                "align-self": "center",
                                "background-color": "white",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    fluid=True,
                )
            ],
        )

    def _layout_body_card(self):
        return [
            dmc.Card(
                children=[
                    dmc.CardSection(
                        self._divider_top(),
                        withBorder=False,
                        # inheritPadding=True,
                        # mt="sm",
                        # mr="sm",
                        style={
                            "align": "top",
                            "background-color": "white",
                            # "margin-top": "-20px",
                        },
                    ),
                    dmc.CardSection(
                        children=self.form(),
                        withBorder=True,
                        inheritPadding=False,
                        # mr=0,
                        # ml=0,
                        style={
                            # "width": "100%",
                            # "height": "100%",
                            "align-self": "center",
                            "justify-content": "center",
                            "background-color": card_color,
                        },
                    ),
                    dmc.CardSection(
                        self._divider(),
                        withBorder=False,
                        inheritPadding=True,
                        # mt="sm",
                        # mr="sm",
                        style={
                            "align": "center",
                            "background-color": "white",
                        },
                    ),
                    dmc.CardSection(
                        self._layout_cardfooter(),
                        withBorder=False,
                        inheritPadding=True,
                        # mt="sm",
                        # mr=0,
                        style={
                            # "width": "100%",
                            # "height": "100%",
                            "align-self": "top",
                            "justify-content": "center",
                            "background-color": "white",
                        },
                    ),
                ],
                withBorder=False,
                # shadow="sm",
                # radius="md",
                # mr=0,
                style={
                    "width": "100%",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": card_color,
                    "justify-content": "center",
                },
                # className="d-flex justify-content-center",
            )
        ]

    def form(self):
        return dmc.Card(
            [
                self.alert(),
                self.alert_error(),
                dbc.Form(
                    [
                        self.firstname_input(),
                        self.lastname_input(),
                        self.email_input(),
                        self.text_input(),
                    ]
                ),
                self.submit(),
            ],
            withBorder=False,
            # shadow="sm",
            # radius="md",
            # mr=0,
            style={
                "width": "100%",
                "height": "100%",
                "align-self": "center",
                "background-color": card_color,
                "justify-content": "center",
            },
            # className="d-flex justify-content-center",
        )

    def firstname_input(self):
        return dbc.Row(
            html.Div(
                [
                    dbc.Label("Vorname"),
                    dbc.Input(type="firstname", id="firstname", placeholder="Vorname"),
                ],
                className="mb-3",
            )
        )

    def lastname_input(self):
        return dbc.Row(
            html.Div(
                [
                    dbc.Label("Nachname"),
                    dbc.Input(type="lastname", id="lastname", placeholder="Nachname"),
                ],
                className="mb-3",
            )
        )

    def email_input(self):
        return dbc.Row(
            html.Div(
                [
                    dbc.Label("Email", html_for="example-email"),
                    dbc.Input(type="email", id="email", placeholder="E-mail Adresse"),
                    # dbc.FormText(
                    #     "Are you on email? You simply have to be these days",
                    #     color="secondary",
                    # ),
                ],
                className="mb-3",
            )
        )

    def text_input(self):
        return dbc.Row(
            html.Div(
                [
                    dbc.Label("Nachricht", html_for="text"),
                    dbc.Input(type="text", id="text", placeholder="Was kann ich für Sie tun?"),
                ],
                className="mb-3",
            )
        )

    def submit(self):
        return dbc.Row(
            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "margin-top": "20px",
                    "margin-bottom": "20px",
                    "background-color": "card_color",
                },
                children=[
                    dmc.Button(
                        "Abschicken",
                        id="submit-button",
                        variant="outline",
                        disabled=True,
                        rightIcon=DashIconify(icon="ic:baseline-email", width=20),
                        # color="lightgray",
                        # style={
                        #     "font-family": headline["font-family"],
                        #     "align": "center",
                        #     "color": "black",
                        #     "font-size": "20px",
                        #     "background-color": card_color,
                        #     "box-shadow": "5px 5px 7px rgba(0, 0, 0, 0.6)",
                        # },
                    )
                ],
            )
        )

    def alert(self):
        return dmc.Alert(
            "Das Kontaktformular wurde erfolgreich verschickt. Ich melde mich in Kürze bei Ihnen.",
            title="Erfolgreich verschickt!",
            id="alert-dismiss",
            color="green",
            withCloseButton=True,
            hide=True,
        )

    def alert_error(self):
        return dmc.Alert(
            "Ein Problem ist aufgeteten. Bitte schicken Sie Ihre Nachricht per Email an kontakt@beas-coaching.de.",
            title="Error!",
            id="alert-dismiss_error",
            color="red",
            withCloseButton=True,
            hide=True,
        )
