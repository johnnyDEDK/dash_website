import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..ui.layout import FrontEndLayout

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
card_color = "#edf1fa"  # "#EDEBE7"
accordion_color = card_color  # "-#D6DCE5"  # "#F8F9FA"
textfont = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black"}


class Company(FrontEndLayout):
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
                        children=[
                            dmc.SimpleGrid(
                                cols=1,
                                children=self._layout_cardheader_second_row(
                                    image="assets/board-4855932_1920.jpg",
                                    text_content=self._header_list(
                                        text1=["Als Führungskraft"], text2=self._header_text_2()
                                    ),
                                ),
                                # mt="sm",
                                breakpoints=[
                                    {"minWidth": 1001, "maxWidth": 10000, "cols": 2},
                                    {"minWidth": 600, "maxWidth": 1000, "cols": 1},
                                ],
                                style={
                                    "align-self": "center",
                                    "justify-content": "center",
                                    "background-color": card_color,
                                },
                            ),
                        ],
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
                        self._layout_cardbody2(),
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
                        children=[
                            dmc.SimpleGrid(
                                cols=1,
                                children=self._third_row(),
                                # mt="sm",
                                breakpoints=[
                                    {"minWidth": 1001, "maxWidth": 10000, "cols": 2},
                                    {"minWidth": 600, "maxWidth": 1000, "cols": 1},
                                ],
                                style={
                                    "align-self": "center",
                                    "justify-content": "end",
                                    "background-color": card_color,
                                },
                            ),
                        ],
                        withBorder=True,
                        inheritPadding=False,
                        # mr=0,
                        # ml=0,
                        style={
                            # "width": "100%",
                            # "height": "100%",
                            "align-self": "center",
                            "justify-content": "end",
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

    def _layout_cardbody(self):
        return [
            self._layout_cardbody_zero_row(),
            self._layout_cardbody_first_row(),
            self._layout_cardbody_second_row(),
            self._layout_cardbody_third_row(),
        ]

    def _layout_cardbody2(self):
        return [
            self._layout_cardbody_fourth_row(),
            self._layout_cardbody_fifth_row(),
            self._layout_cardbody_sixth_row(),
        ]

    def _layout_cardbody_zero_row(self):
        return dbc.Row(dbc.Col(self._main_text_0(), width=7), justify="center")

    def _layout_cardbody_first_row(self):
        return dbc.Row(self._main_text_1(), style={"justify-content": "center", "align-content": "center"})

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._main_text_2()])

    def _layout_cardbody_third_row(self):
        return dbc.Row([self._main_text_3()])

    def _layout_cardbody_fourth_row(self):
        return dbc.Row([self._main_text_4()])

    def _layout_cardbody_fifth_row(self):
        return dbc.Row([self._main_text_5()])

    def _layout_cardbody_sixth_row(self):
        return dbc.Row([self._main_text_6()])

    def _header_list(self, text1, text2):
        return dbc.Row(
            dbc.Col(
                [
                    dbc.Row(
                        dcc.Markdown(
                            text1,
                            style={
                                "font-family": textfont["font-family"],
                                "align": "left",
                                "overflow": "hidden",
                                "textOverflow": "ellipsis",
                                # "margin-bottom": "-20px",
                                "margin-top": "20px",
                                "margin-right": "-20px",
                                "margin-left": "0px",
                                "margin": "0px",
                                "line-height": "1.1",
                                # "display": "flex",
                                "justify-content": "center",
                            },
                            className="markdown-responsive align-content-center justify-content-center",
                        ),
                        justify="center",
                        className="align-content-center justify-content-center",
                    ),
                    dbc.Row(
                        dcc.Markdown(
                            text2,
                            style={
                                "font-family": textfont["font-family"],
                                "align": "left",
                                "overflow": "hidden",
                                "textOverflow": "ellipsis",
                                "margin-bottom": "-18px",
                                "margin-top": "60px",
                                "margin-right": "-20px",
                                "margin-left": "0px",
                                "margin": "-20px",
                                "line-height": "1.1",
                                # "display": "flex",
                                "justify-content": "center",
                            },
                            className="markdown-responsive align-content-center justify-content-center",
                        ),
                        justify="center",
                        className="align-content-center justify-content-center",
                        style={"margin-top": "20px", "margin-left": "-25px"},
                    ),
                ],
                align="center",
                className="align-content-center justify-content-center",
            ),
            justify="center",
            className="align-content-center justify-content-center",
        )

    def _header_text_2(self):
        return [
            """\n* Möchten Sie eine Veränderung erwirken und ihr Team dabei optimal einbinden.""",
            """\n* Registrieren Sie einen gewissen Vorbehalt gegenüber einer anstehenden/ laufenden Veränderung.""",
            """\n* Stehen Sie mit ihrem Team vor einer größeren strukturellen Veränderung.""",
        ]

    def _main_text_0(self):
        return [
            dcc.Markdown(
                [
                    """*„Eine Gruppe ist mehr als die Summe ihrer einzelnen Mitglieder.“*""",
                ],
                style={
                    "font-family": textfont["font-family"],
                    "margin-bottom": "0px",
                    "margin-top": "20px",
                    "background-color": card_color,
                    "align-self": "center",
                    "justify-content": "center",
                    "line-height": "1.1",
                },
                className="markdown-responsive",
            ),
        ]

    def _main_text_1(self):
        return [
            dcc.Markdown(
                [
                    """ \n \n Dieser Satz fällt häufig. Es wir jedoch kaum darüber gesprochen, dass es auch das Gegenteil gibt: eine Gruppe kann weniger sein als die Summe ihrer einzelnen Mitglieder.""",
                    """ \n Zum Beispiel dann, wenn Rollen nicht klar definiert sind, nicht alle das gleiche Ziel verfolgen oder Konflikte zwischen einzelnen Mitgliedern bestehen. Da Teams, Abteilungen und Unternehmen einer ständigen Veränderung (personell, sich ändernde Anforderungen oder Rahmenbedingungen) unterworfen sind, kann dies sogar schnell passieren.""",
                ],
                style={
                    "font-family": textfont["font-family"],
                    "margin-bottom": "0px",
                    "margin-top": "20px",
                    "background-color": card_color,
                    "align-self": "center",
                    "justify-content": "center",
                    "line-height": "1.1",
                },
                className="markdown-responsive",
            ),
        ]

    def _main_text_2(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """ \n \n Nun ist Kommunikation gefragt. Diese wird bei einem Team Coaching in einem geschützten Raum gestaltet. Dabei wird ganz individuell auf die Bedürfnisse der Gruppe eingegangen.""",
                        """ \n \n Im organisatorischen Kontext betrachtet man drei Ebenen:""",
                        """ \n* Jedes einzelne Gruppenmitglied hat menschliche Bedürfnisse wie Weiterentwicklung, Sicherheit oder Anerkennung.""",
                        """ \n* Es gibt jedoch auch Anforderungen, die die Rolle in der Organisation mit sich bringt (fachlich wie disziplinarisch) und zudem  """,
                        """ \n* hat die Organisation Erwartungen an jedeN ihreR MitarbeiterInnen. """,
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "margin-bottom": "0px",
                        "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "center",
                        "line-height": "1.1",
                    },
                    className="markdown-responsive",
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

    def _main_text_3(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """ \n \n Alle drei Ebenen sind im Team-Coaching wichtig und spielen bei der Ausgestaltung des Konzepts eine Rolle.""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "margin-bottom": "0px",
                        "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "center",
                        "line-height": "1.1",
                    },
                    className="markdown-responsive",
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

    def _main_text_4(self):
        return dbc.Container(
            [
                dbc.Row(
                    self.markdown_text("## Beispiele, wann ein Team-Coaching sinnvoll sein kann", weight="bold"),
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                "margin-top": "20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def _main_text_5(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """ \n* Hohe Fluktuation im Team, was z.B. zu ungeklärten Verantwortungen führt.""",
                        """ \n* Neue Führungskraft, vielleicht sogar aus dem Team kommend.""",
                        """ \n* Es liegt fachlich eine größere Veränderung vor und das Team hat Angst, das bestehende loszulassen.""",
                        """ \n* Andere Veränderungen am Arbeitsplatz, die zu einem Kontrollverlustgefühl bei den Teammitgliedern führt.""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "margin-bottom": "20px",
                        "margin-top": "10px",
                        "background-color": card_color,
                        "align-self": "center",
                        "line-height": "1.1",
                    },
                    className="markdown-responsive",
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

    def _main_text_6(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Gemeinsam mit dem Auftragsgeber wird im Vorfeld die Situation ausführlich besprochen.""",
                        """Basierend auf diesem Gespräch erstelle ich ein Konzept, welches vor der Umsetzung besprochen wird.""",
                        """\n In der Umsetzungsphase wird situativ reagiert und das Konzept an die Bedürfnisse und das Verhalten der gesamten Gruppe angepasst.""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "margin-bottom": "0px",
                        "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "center",
                        "line-height": "1.1",
                    },
                    className="markdown-responsive",
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

    def _third_row(self):
        return [
            dmc.Card(
                [
                    dmc.CardSection(
                        self._third_card_text(),
                        inheritPadding=True,
                        className="d-flex justify-content-center align-content-center",
                        style={"align": "center", "background-color": card_color, "margin-top": "20px"},
                    ),
                    # dmc.CardSection(
                    #     self._free_contact(),
                    #     # py="xl",
                    #     style={
                    #         "align": "center",
                    #         "background-color": card_color,
                    #     },
                    #     inheritPadding=True,
                    # ),
                ],
                style={
                    # "width": "100%",
                    # "height": "100%",
                    "align-self": "top",
                    "background-color": card_color,
                    "justify-content": "center",
                },
            ),
            dmc.Image(
                src=self.path + "assets/darts-102919_1920_quadrat.jpg",
                # className="d-flex justify-content-end",
                style={
                    "width": "100%",
                    "maxWidth": "800px",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": card_color,
                    "justify-content": "end",
                    "@media screen and (min-width: 768px)": {"maxWidth": "500px", "height": "auto"},
                },
            ),
        ]

    def _third_card_text(self):
        return dbc.Container(
            [self._third_card_text_1(), self._third_card_text_2(), self._third_card_text_3()],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                "margin-top": "-20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "top",
            },
        )

    def _third_card_text_1(self):
        return dbc.Row(
            self.markdown_text("## Ziele des Team-Coachings", weight="bold"),
        )

    def _third_card_text_2(self):
        return dbc.Row(
            dcc.Markdown(
                [
                    """Unabhängig vom Anlass, gibt es generelle Ziele beim Team-Coaching, u.a.:""",
                ],
                style={
                    "font-family": textfont["font-family"],
                    "margin-bottom": "-20px",
                    "margin-top": "0px",
                    "background-color": card_color,
                    "align-self": "center",
                },
                className="markdown-responsive",
            )
        )

    def _third_card_text_3(self):
        return dbc.Row(
            dcc.Markdown(
                [
                    """ \n* Steigerung der Team-effizienz und -effektivität""",
                    """ \n* Identifikation und Entwicklung von Team-Stärken (damit die Gruppe wieder mehr ist als Summe der Einzelteile)""",
                    """ \n* Raum für Reflexion und neue Impulse schaffen""",
                    """ \n* Jedem Teammitglied das Gefühl geben, eine Veränderung selbst gestalten zu können""",
                ],
                style={
                    "font-family": textfont["font-family"],
                    "margin-bottom": "0px",
                    "margin-top": "10px",
                    "background-color": card_color,
                    "align-self": "top",
                },
                className="markdown-responsive",
            )
        )

    def markdown_text(self, text, weight="normal"):
        return dbc.Container(
            [
                dcc.Markdown(
                    text,
                    style={
                        "font-family": textfont["font-family"],
                        "font-weight": weight,
                        # "margin-bottom": "20px",
                        # "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "top",
                        "line-height": "1.1",
                    },
                    className="markdown-responsive",
                )
            ],
            fluid=True,
            style={
                "margin-bottom": "10px",
                "margin-top": "0px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "top",
            },
        )
