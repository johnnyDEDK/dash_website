import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
accordion_color = "#D6DCE5"  # "#F8F9FA"


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
                "fontFamily": "Georgia",
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
                                        "background-color": "#D6DCE5",
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
                                    "background-color": "#D6DCE5",
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
                            "background-color": "#D6DCE5",
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
                            "background-color": "#D6DCE5",
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
                            "background-color": "#D6DCE5",
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
                    "background-color": "#D6DCE5",
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
                    "background-color": "#D6DCE5",
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
                        style={"align": "center", "background-color": "#D6DCE5", "margin-top": "20px"},
                    ),
                    dmc.CardSection(
                        self._free_contact(),
                        # py="xl",
                        style={
                            "align": "center",
                            "background-color": "#D6DCE5",
                        },
                        inheritPadding=True,
                    ),
                ],
                style={
                    "width": "100%",
                    "height": "100%",
                    "align-self": "center",
                    "background-color": "#D6DCE5",
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
        return dbc.Row([self._landing_page_text()])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._free_contact()])

    def _layout_cardbody_third_row(self):
        return dbc.Row(self.accordion_card())

    def _layout_cardfooter(self):
        return self._carousel()

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
                dcc.Markdown(
                    [
                        """Sie """,
                        """\n* stehen Privat oder im Beruf vor einer Veränderung.""",
                        """\n* sind Führungskraft oder Unternehmer und mit ihrem Team im Veränderungsprozess.""",
                        """\n* möchten eine Veränderung in Ihrem Leben erwirken.""",
                    ],
                    style={
                        "font-family": "Georgia",
                        "align": "left",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "margin-bottom": "-20px",
                        "margin-top": "20px",
                        "margin-right": "-20px",
                        "margin": "0px",
                        "line-height": "1.1",
                        # "display": "flex",
                        "justify-content": "center",
                    },
                    className="markdown-responsive align-content-center justify-content-center",
                ),
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
                "margin-bottom": "20px",
                "background-color": "#D6DCE5",
            },
            children=[
                dmc.Anchor(
                    dmc.Button(
                        dcc.Markdown(
                            "Kostenfreies Erstgespräch",
                            style={
                                "font-family": "Georgia",
                                # "margin-bottom": "20px",
                                "margin-top": "20px",
                                "background-color": "#D6DCE5",
                                "align-self": "center",
                            },
                            className="markdown-responsive",
                        ),
                        variant="outline",
                        rightIcon=DashIconify(icon="ic:baseline-email", width=20),
                        color="lightgray",
                        style={
                            "font-family": "Georgia",
                            "align": "center",
                        },
                    ),
                    href="mailto:beatrice_koch@gmx.de?subject=Kostenlose Erstkontakt",
                )
            ],
        )

    def _landing_page_text(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Ich coache, um Sie bei herausfordernden Situationen systemisch zu unterstützen.""",
                        """  \n  \n Gemeinsam betrachten wir Ihre Situation „von außen“. Mit dem damit gewonnenen Abstand erlangen Sie neue Perspektiven. Und damit einhergehend eine Erweiterung Ihrer Handlungs-, Denk- und Haltungsoptionen.""",
                        """ \n \n Ich coache nach dem systemisch-konstruktivistischen Ansatz. Methoden aus verschiedenen Ansätzen, zum Beispiel aus der Gestaltung, finden bei mir Anwendung. Damit verfolge ich eine wissenschaftlich fundierte Herangehensweise im Coaching.""",
                        """ \n \n Ich freue mich darauf, Sie bei einem unverbindlichen Kennenlerngespräch näher kennen zu lernen!""",
                        """ \n \n Ihre _Beatrice Koch_""",
                    ],
                    style={
                        "font-family": "Georgia",
                        # "margin-bottom": "20px",
                        "margin-top": "20px",
                        "background-color": "#D6DCE5",
                        "align-self": "center",
                    },
                    className="markdown-responsive",
                )
            ],
            fluid=True,
            style={
                # "margin-bottom": "20px",
                # "margin-top": "20px",
                "background-color": "#D6DCE5",
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
                            "01 - Unverbindliches Kennenlern-Gespräch",
                            icon=DashIconify(
                                icon="icon-park-solid:info",
                                # color=dmc.theme.DEFAULT_COLORS["blue"][6],
                                width=25,
                            ),
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
        return self.path + "assets/01.png"

    def accordion_image2(self):
        return self.path + "assets/02.png"

    def accordion_image3(self):
        return self.path + "assets/03.png"

    def accordion_card(self):
        return dmc.Card(
            [
                dmc.CardSection(
                    self._accordion_header(),
                    inheritPadding=False,
                    className="d-flex justify-content-center align-content-center",
                    style={
                        "align": "center",
                        "background-color": "#D6DCE5",
                        "margin-top": "10px",
                    },
                ),
                dmc.CardSection(
                    self._accordion(),
                    # py="xl",
                    style={
                        "align": "center",
                        "background-color": "#D6DCE5",
                    },
                    inheritPadding=False,
                ),
            ],
            style={
                "align-self": "center",
                "background-color": "#D6DCE5",
                "justify-content": "center",
            },
        )

    def _accordion_header(self):
        return dbc.Row(
            dbc.Col(
                dcc.Markdown(
                    """#### Ablauf eines Coachings""",
                    style={
                        "font-family": "Georgia",
                        "align": "left",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "margin-bottom": "-20px",
                        "margin-top": "20px",
                        "margin-right": "-20px",
                        "margin": "0px",
                        "line-height": "1.1",
                        # "display": "flex",
                        "justify-content": "center",
                    },
                    # className="markdown-responsive align-content-center justify-content-center",
                ),
                align="center",
                className="align-content-center justify-content-center",
            ),
            justify="center",
            className="align-content-center justify-content-center",
        )

    def _accordion_text(self, text):
        return dbc.Container(
            dcc.Markdown(
                text,
                style={
                    "font-family": "Georgia",
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
            """ \n \n Nach dem Gespräch haben Sie:""",
            """ \n* Ein Gefühl für meine Arbeitsweise.""",
            """ \n* Antworten zu inhaltlichen, organisatorischen und sonstigen Fragen.""",
            """ \n* Eine Vorstellung, wie wir Ihr Anliegen in den Sitzungen behandeln.""",
        ]

    def _accordion_item2_text(self):
        return [
            """Jedes Anliegen ist so persönlich und individuell wie ihr Träger. Daher biete ich keine vordefinierten Pakete an.""",
            """  \n  \n Informationen zu den Sitzungen:""",
            """ \n* 50 oder 90min – wir entscheiden gemeinsam.""",
            """ \n* Die Frequenz variiert je nach Anliegen.""",
            """ \n 2-3 Sitzungen mit kürzerem Abstand sind z.B. bei akuten Phasen hilfreich. Bei einer Begleitung sind größere zeitliche Abständen mit mehr Zeit zur Erfahrung und Anwendung der Erkenntnisse im Alltag zielführend.""",
            """ \n* Die Sitzungen können digital, in Präsenz oder hybrid („mal so, mal so“) stattfinden.""",
        ]

    def _accordion_item3_text(self):
        return [
            """Eine Abschlusssitzung ist vor allem bei längeren Veränderungsphasen hilfreich.""",
            """ \n \n Hier reflektieren wir Ihre Entwicklungsschritte und gehen die Erkenntnisse der Sitzungen nochmal gemeinsam durch.""",
            """  \n  \n Gerade im beruflichen Kontext ist es sinnvoll, die Führungskraft und Personalverantwortlichen sowohl vorab, als auch zur Abschlusssitzung einzubeziehen. So stellen wir eine Unterstützung Ihres beruflichen Umfelds während und nach des Coachings sicher.""",
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
