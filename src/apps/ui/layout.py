import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from pytest import mark
from requests import head
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
card_color = "#EDEBE7"
accordion_color = card_color  # "-#D6DCE5"  # "#F8F9FA"
textfont = {"font-family": "Karla", "color": "black"}
headline = {"font-family": "Karla", "color": "black"}


class FrontEndLayout(DashBasePage):
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
                                    xl={"size": 10},  # , "offset": 1},
                                    xxl={"size": 7},  # , "offset": 1},
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
                                "margin-top": "-5px",
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
                                children=self._layout_cardheader_second_row(),
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
                        self._layout_cardbody_third_row(),
                        withBorder=False,
                        inheritPadding=True,
                        # mt="sm",
                        # mr=0,
                        style={
                            "align-self": "center",
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
                        self.references(),
                        withBorder=False,
                        inheritPadding=True,
                        # mt="sm",
                        # mr=0,
                        style={
                            "align-self": "center",
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
                src=self.path + "assets/Unbenannt.png",
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
                            "margin-top": "40px",
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
        return dbc.Row([self.markdown_text(self._landing_page_text())])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._free_contact()])

    def _layout_cardbody_third_row(self):
        return dbc.Row(self.accordion_card())

    def _third_header(self):
        return dmc.Container(
            dmc.SimpleGrid(
                cols=1,
                children=[self._header_list(), self._free_contact()],
                breakpoints=[
                    {"minWidth": 980, "maxWidth": 2000, "cols": 1},
                    {"minWidth": 755, "maxWidth": 979, "cols": 2},
                    {"minWidth": 600, "maxWidth": 754, "cols": 1},
                ],
                verticalSpacing=0,
                style={
                    "display": "flex",
                    "justify-content": "center",
                },
            ),
            size="auto",
            style={
                "display": "flex",
                "justify-content": "center",
            },
        )

    def _header_list(self):
        return dbc.Row(
            dbc.Col(
                [
                    dbc.Row(
                        dcc.Markdown(
                            ["""Sie """],
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
                            [
                                """\n* stehen Privat oder im Beruf vor einer Veränderung.""",
                                """\n* sind Führungskraft oder Unternehmer und mit ihrem Team im Veränderungsprozess.\n""",
                                """* möchten eine Veränderung in Ihrem Leben erwirken.""",
                            ],
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

    def _free_contact(self):
        return html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "margin-top": "20px",
                "margin-bottom": "20px",
                "background-color": "card_color",
            },
            children=[
                dmc.Anchor(
                    dmc.Button(
                        dcc.Markdown(
                            "Kostenfreies Erstgespräch",
                            style={
                                "font-family": headline["font-family"],
                                # "margin-bottom": "20px",
                                "margin-top": "20px",
                                "background-color": "white",
                                "align-self": "center",
                            },
                            className="markdown-responsive",
                        ),
                        variant="outline",
                        rightIcon=DashIconify(icon="ic:baseline-email", width=20),
                        color="lightgray",
                        style={
                            "font-family": headline["font-family"],
                            "align": "center",
                            "color": "black",
                            "font-size": "20px",
                            "background-color": "white",
                            "box-shadow": "5px 5px 7px rgba(0, 0, 0, 0.6)",
                        },
                    ),
                    href="mailto:beatrice_koch@gmx.de?subject=Kostenlose Erstkontakt",
                )
            ],
        )

    def _landing_page_text(self):
        return [
            """Ich coache, um Sie bei herausfordernden Situationen systemisch zu unterstützen.""",
            """  \n  \n Gemeinsam betrachten wir Ihre Situation „von außen“. Mit dem damit gewonnenen Abstand erlangen Sie neue Perspektiven. Und damit einhergehend eine Erweiterung Ihrer Handlungs-, Denk- und Haltungsoptionen.""",
            """ \n \n Ich coache nach dem systemisch-konstruktivistischen Ansatz. Methoden aus verschiedenen Ansätzen, zum Beispiel aus der Gestaltung, finden bei mir Anwendung. Damit verfolge ich eine wissenschaftlich fundierte Herangehensweise im Coaching.""",
            """ \n \n Ich freue mich darauf, Sie bei einem unverbindlichen Kennenlerngespräch näher kennen zu lernen!""",
            """ \n \n Ihre _Beatrice Koch_""",
        ]

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
                        "align-self": "center",
                    },
                    className="markdown-responsive",
                )
            ],
            fluid=True,
            style={
                "margin-bottom": "20px",
                "margin-top": "20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def _carousel(self):
        return dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": self.path + "assets/Website_Schritte-Coaching_01.png",
                },
                {"key": "2", "src": self.path + "assets/Website_Schritte-Coaching_02.png"},
                {"key": "3", "src": self.path + "assets/Website_Schritte-Coaching_03.png"},
            ],
            controls=True,
            indicators=True,
        )

    def _accordion(self):
        return dmc.Accordion(
            disableChevronRotation=True,
            # variant="contained",
            className="g0",
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(
                            "01 - Unverbindliches Kennenlerngespräch",
                            icon=DashIconify(
                                icon="icon-park-solid:info",
                                # color=dmc.theme.DEFAULT_COLORS["blue"][6],
                                width=25,
                            ),
                            style={"font-family": headline["font-family"]},
                        ),
                        dmc.AccordionPanel(
                            self._accordion_grid(
                                self.accordion_image1(), self.accordion_content(self._accordion_item1_text())
                            )
                        ),
                    ],
                    value="info1",
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(
                            "02 - Sitzungen",
                            icon=DashIconify(
                                icon="icon-park-solid:info",
                                # color=dmc.theme.DEFAULT_COLORS["blue"][6],
                                width=25,
                            ),
                        ),
                        dmc.AccordionPanel(
                            self._accordion_grid(
                                self.accordion_image2(), self.accordion_content(self._accordion_item2_text())
                            )
                        ),
                    ],
                    value="info2",
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(
                            "03 - Optionales Abschlussgespräch",
                            icon=DashIconify(
                                icon="icon-park-solid:info",
                                # color=dmc.theme.DEFAULT_COLORS["blue"][6],
                                width=25,
                            ),
                        ),
                        dmc.AccordionPanel(
                            self._accordion_grid(
                                self.accordion_image3(), self.accordion_content(self._accordion_item3_text())
                            )
                        ),
                    ],
                    value="info3",
                ),
            ],
            style={"width": "100%"},
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

    def accordion_content(self, content):
        return (
            dmc.Card(
                dmc.CardSection(
                    self._accordion_text(content),
                    inheritPadding=True,
                    className="d-flex justify-content-center align-content-center",
                    style={"align": "center", "background-color": accordion_color},
                ),
                style={
                    "width": "100%",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": accordion_color,
                    "justify-content": "center",
                },
            ),
        )

    def accordion_image(self, image):
        return dmc.Image(
            src=image,
            style={
                "width": "100%",
                "height": "100%",
                "align-self": "center",
                "background-color": accordion_color,
                "justify-content": "center",
            },
        )

    def accordion_image1(self):
        return self.path + "assets/Handshake_2.jpg"

    def accordion_image2(self):
        return self.path + "assets/Kalender2.jpg"

    def accordion_image3(self):
        return self.path + "assets/yes-hand.PNG"

    def accordion_card(self):
        return dmc.Card(
            [
                dmc.CardSection(
                    self.markdown_text(self._accordion_header(), weight="bold"),
                    inheritPadding=True,
                    # className="d-flex justify-content-center align-content-center",
                    style={
                        "align": "center",
                        "background-color": card_color,
                        # "margin-top": "10px",
                        # "margin-bottom": "20px",
                    },
                ),
                dmc.CardSection(
                    self.timeline(),
                    # py="xl",
                    style={
                        "align": "center",
                        "margin-bottom": "20px",
                        "background-color": card_color,
                    },
                    inheritPadding=True,
                ),
            ],
            style={
                "align-self": "center",
                "background-color": card_color,
                "justify-content": "center",
            },
        )

    def _accordion_header(self):
        return """### Ablauf eines Coachings"""
        # return dbc.Row(
        #     dbc.Col(
        #         dcc.Markdown(
        #             """#### Ablauf eines Coachings""",
        #             style={
        #                 "font-family": headline["font-family"],
        #                 "align": "left",
        #                 "overflow": "hidden",
        #                 "textOverflow": "ellipsis",
        #                 "margin-bottom": "-20px",
        #                 "margin-top": "20px",
        #                 "margin-right": "-20px",
        #                 "margin": "0px",
        #                 "line-height": "1.1",
        #                 # "display": "flex",
        #                 "justify-content": "start",
        #             },
        #             # className="markdown-responsive align-content-center justify-content-center",
        #         ),
        #         align="left",
        #     ),
        #     justify="start",
        #     className="align-content-left justify-content-start",
        # )

    def _accordion_text(self, text):
        return dbc.Container(
            dcc.Markdown(
                text,
                style={
                    "font-family": textfont["font-family"],
                    # "margin-bottom": "20px",
                    # "margin-top": "20px",
                    "background-color": accordion_color,
                    "width": "100%",
                    "height": "100%",
                    "align-self": "center",
                },
                className="markdown-responsive",
            ),
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": accordion_color,
                "width": "100%",
                "height": "100%",
                "align-self": "center",
            },
        )

    def _accordion_item1_text(self):
        return [
            """Bevor Sie sich entscheiden, lernen wir uns kennen.""",
            """  \n  \n Das Gespräch dauert ca. 30min und kann telefonisch, per Video-Telefonie oder in Präsenz stattfinden.""",
        ]

    def _accordion_item2_text(self):
        return [
            """Jedes Anliegen ist so individuell wie ihr*e Träger\*in. Daher biete ich keine vordefinierten Pakete an. Eine Sitzung dauert 50 oder 90min. Die Frequenz variiert je nach Anliegen. """,
        ]

    def _accordion_item3_text(self):
        return [
            """Eine Abschlusssitzung ist bei längeren Veränderungsphasen hilfreich. Wir reflektieren Ihre Entwicklungs-schritte und gehen die Erkenntnisse der Sitzungen gemeinsam durch.""",
        ]

    def _accordion_grid(self, image, content):
        return dmc.SimpleGrid(
            cols=1,
            children=[self.accordion_image(image), content[0]],
            # mt="sm",
            breakpoints=[
                {"minWidth": 1001, "maxWidth": 10000, "cols": 2},
                {"minWidth": 600, "maxWidth": 1000, "cols": 1},
            ],
            style={
                "align-self": "center",
                "width": "100%",
                "height": "100%",
                "justify-content": "center",
                "background-color": accordion_color,
            },
        )

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

    def timeline(self):
        return dmc.Timeline(
            id="timeline",
            active=1,
            bulletSize=20,
            lineWidth=2,
            children=[
                self.timeline_item(
                    "Unverbindliches Kennenlerngespräch",
                    self._accordion_grid(self.accordion_image1(), self.accordion_content(self._accordion_item1_text())),
                    id="info1",
                ),
                self.timeline_item(
                    "Sitzungen",
                    self._accordion_grid(self.accordion_image2(), self.accordion_content(self._accordion_item2_text())),
                    id="info2",
                ),
                self.timeline_item(
                    "Optionales Abschlussgespräch",
                    self._accordion_grid(self.accordion_image3(), self.accordion_content(self._accordion_item3_text())),
                    id="info3",
                ),
            ],
        )

    def timeline_item(self, title, children, id):
        return dmc.TimelineItem(
            title=self.markdown_text(title),
            children=[
                dmc.Text(
                    [
                        dmc.Spoiler(
                            showLabel="Show",
                            hideLabel="Hide",
                            initialState=False,
                            maxHeight=0,
                            children=[children],
                            id=id,
                        ),
                    ],
                    color="dimmed",
                    # size="sm",
                ),
            ],
            style={"font-family": headline["font-family"], "font-weight": "normal"},
        )

    def markdown_responsive_small(self, text, weight="normal"):
        dbc.Container(
            [
                dcc.Markdown(
                    text,
                    style={
                        "font-family": textfont["font-family"],
                        "font-weight": weight,
                        # "margin-bottom": "20px",
                        # "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "center",
                    },
                    className="markdown-responsive",
                )
            ],
            fluid=True,
            style={
                "margin-bottom": "20px",
                "margin-top": "20px",
                "background-color": card_color,
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def references(self):
        return [
            dbc.Row(
                self.markdown_text("""### Referenzen""", weight="bold"),
                style={
                    "align": "center",
                    "background-color": card_color,
                    # "margin-top": "10px",
                    # "margin-bottom": "20px",
                },
            ),
            dbc.Row(
                dmc.Card(
                    self._first_ref(),
                    withBorder=False,
                    style={
                        # "margin-bottom": "20px",
                        # "margin-top": "20px",
                        "background-color": card_color,
                        # "width": "100%",
                        # "height": "100%",
                        "align-self": "center",
                    },
                )
            ),
            dbc.Row(
                dmc.Card(
                    self._second_ref(),
                    withBorder=False,
                    style={
                        # "margin-bottom": "20px",
                        # "margin-top": "20px",
                        "background-color": card_color,
                        # "width": "100%",
                        # "height": "100%",
                        "align-self": "center",
                    },
                )
            ),
        ]

    def _first_ref(self):
        return dbc.Container(
            [
                dmc.Blockquote(
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        initialState=False,
                        maxHeight=70,
                        children="Mit Beatrice findet man eine Begleitung fürs Leben. Durch ihre ruhige Art gibt sie Sicherheit. Sie schafft es, dem Klienten in seinem Anliegen zu folgen und gleichzeitig zu führen. Sie kann sehr gut zuhören und begleitet die eigene Entwicklung professionell und sehr klar. Die Anwendung vielfältiger Methoden hilft auch aus komplexen Situationen einen Ausweg zu finden. Ihre offen und unkomplizierte Art macht es einem sehr leicht sich zu öffnen und auch schwierige Dinge auszusprechen.",
                        id="ref1",
                    ),
                    cite="- Annika",
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": "white",
                # "border-radius": "2em",
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )

    def _second_ref(self):
        return dbc.Container(
            [
                dmc.Blockquote(
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        initialState=False,
                        maxHeight=70,
                        children="Beatrice hat mir geholfen, mit einem liebevollen und urteilsfreien Blick auf meine Herausforderungen zu sehen. Während ich vor den gemeinsamen Coaching-Sessions wahnsinnig harsch über mich selbst geurteilt und mich ständig mit anderen Menschen verglichen habe, lösten die Gespräche mit Beatrice einen Perspektivwechsel in mir aus. Ihre Art, meine existierende Sichtweisen zu hinterfragen und alternative Szenarien und Interpretationen in den Raum zu stellen, lässt mich sowohl mich selbst, als auch die Welt um mich herum, offener betrachten. Gemeinsam haben wir Konzepte erarbeitet, die mir helfen, mit Selbstzweifeln und Perfektionismus kurzfristig umzugehen und langfristig bestehende Muster zu durchrechen.",
                        id="ref1",
                    ),
                    cite="- Laura",
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": "white",
                # "border-radius": "2em",
                # "width": "100%",
                # "height": "100%",
                "align-self": "center",
            },
        )
