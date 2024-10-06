import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
card_color = "#edf1fa"  # "#EDEBE7"
accordion_color = card_color  # "-#D6DCE5"  # "#F8F9FA"
textfont = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black"}


class References(DashBasePage):
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
                        self._layout_cardbody(),
                        withBorder=True,
                        inheritPadding=True,
                        # mt="sm",
                        # mr=0,
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

    def _layout_cardheader(self):
        return self._layout_cardheader_second_row()

    def _layout_cardheader_second_row(self):
        return [
            dmc.Image(
                src=self.path + "assets/privat.png",
                style={
                    "width": "100%",
                    "maxWidth": "800px",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": card_color,
                    "justify-content": "center",
                    "@media screen and (min-width: 768px)": {"maxWidth": "500px", "height": "auto"},
                },
            ),
            dmc.Card(
                [
                    dmc.CardSection(
                        self._header_list(),
                        inheritPadding=True,
                        className="d-flex justify-content-center align-content-center",
                        style={"align": "center", "background-color": card_color, "margin-top": "20px"},
                    ),
                    dmc.CardSection(
                        self._free_contact(),
                        # py="xl",
                        style={
                            "align": "center",
                            "background-color": card_color,
                        },
                        inheritPadding=True,
                    ),
                ],
                style={
                    "width": "100%",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": card_color,
                    "justify-content": "center",
                },
            ),
        ]

    def _layout_cardbody(self):
        return [
            self._layout_cardbody_first_row(),
            self._layout_cardbody_second_row(),
        ]

    def _layout_cardbody_first_row(self):
        return dbc.Row([self._first_ref()])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._second_ref()])

    def _first_ref(self):
        return dbc.Container(
            [
                dmc.Blockquote(
                    "Mit Beatrice findet man eine Begleitung fürs Leben. Durch ihre ruhige Art gibt sie Sicherheit. Sie schafft es, dem Klienten in seinem Anliegen zu folgen und gleichzeitig zu führen. Sie kann sehr gut zuhören und begleitet die eigene Entwicklung professionell und sehr klar. Die Anwendung vielfältiger Methoden hilft auch aus komplexen Situationen einen Ausweg zu finden. Ihre offen und unkomplizierte Art macht es einem sehr leicht sich zu öffnen und auch schwierige Dinge auszusprechen.",
                    cite="- Annika",
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def _second_ref(self):
        return dbc.Container(
            [
                dmc.Blockquote(
                    "Beatrice hat mir geholfen, mit einem liebevollen und urteilsfreien Blick auf meine Herausforderungen zu sehen. Während ich vor den gemeinsamen Coaching-Sessions wahnsinnig harsch über mich selbst geurteilt und mich ständig mit anderen Menschen verglichen habe, lösten die Gespräche mit Beatrice einen Perspektivwechsel in mir aus. Ihre Art, meine existierende Sichtweisen zu hinterfragen und alternative Szenarien und Interpretationen in den Raum zu stellen, lässt mich sowohl mich selbst, als auch die Welt um mich herum, offener betrachten. Gemeinsam haben wir Konzepte erarbeitet, die mir helfen, mit Selbstzweifeln und Perfektionismus kurzfristig umzugehen und langfristig bestehende Muster zu durchrechen.",
                    cite="- Laura",
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def _divider(self):
        return [
            dbc.Row(
                [
                    dmc.Divider(
                        variant="solid",
                        # color="red",
                        className="g-0",
                        style={
                            "margin-bottom": "20px",
                            "margin-top": "20px",
                            "background-color": "white",
                            #    "align": "center",
                            #    "justify": "center",
                        },
                    )
                ],
                justify="center",
                align="center",
            )
        ]

    def _divider_top(self):
        return [
            dbc.Row(
                [
                    dmc.Divider(
                        variant="solid",
                        # color="red",
                        className="g-0",
                        style={
                            "margin-bottom": "20px",
                            "background-color": "white",
                            #    "align": "center",
                            "justify": "start",
                        },
                    )
                ],
                justify="start",
                align="center",
            )
        ]

    def _layout_cardfooter(self):
        return dbc.Container(
            dmc.Card(
                [
                    dmc.CardSection(
                        [
                            self._footer(self._footer_text1()),
                            self._footer(self._footer_text2()),
                        ],
                        inheritPadding=False,
                        className="d-flex justify-content-evenly align-content-top",
                        style={
                            "align": "top",
                            "background-color": "white",
                            # "margin-top": "10px",
                        },
                    )
                ],
                style={
                    "align-self": "top",
                    "background-color": "white",
                    "justify-content": "center",
                },
            ),
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": "white",
                "align-self": "top",
            },
        )

    def _footer_text1(self):
        return [
            """[Referenzen](/references)""",
        ]

    def _footer_text2(self):
        return [
            """[Impressum](/references)""",
        ]

    def _footer(self, text):
        return dcc.Markdown(
            text,
            style={
                "font-family": textfont["font-family"],
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": "white",
                "width": "100%",
                "height": "100%",
                "align-self": "top",
            },
            className="d-flex justify-content-evenly align-content-evenly markdown-responsive",
        )
