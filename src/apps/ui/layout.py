import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from pytest import mark
from requests import head
from ..utils.dash_base_template import DashBasePage

from typing import Tuple
from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
card_color = "#edf1fa"  # "#dde1ed"  # "rgba(75, 99, 173, .34)"  # "#4b63ad"  # "#EDEBE7"  # "#d2d2d4"  #
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
                                    xl={"size": 8},  # , "offset": 1},
                                    xxl={"size": 6},  # , "offset": 1},
                                    style={
                                        "align-self": "center",
                                        "background-color": "white",
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
                                children=self._layout_cardheader_second_row(
                                    "assets/IMG_0375_quadratisch.JPG",
                                    self._header_list(self.header_text_1(), self.header_text_2()),
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

    def _layout_cardheader_second_row(self, image, text_content):
        return [
            dmc.Image(
                src=self.path + image,
                style={
                    "width": "100%",
                    "maxWidth": "800px",
                    "height": "auto",
                    # "maxHeight": "300px",
                    "align-self": "center",
                    "background-color": card_color,
                    "justify-content": "center",
                    "@media screen and (min-width: 768px)": {
                        "maxWidth": "500px",
                        "height": "auto",
                        "maxHeight": "500px",
                    },
                },
            ),
            dmc.Card(
                [
                    dmc.CardSection(
                        text_content,
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

    def header_text_1(self):
        return ["""Sie"""]

    def header_text_2(self):
        return [
            """\n* stehen privat oder im Beruf vor einer Veränderung.""",
            """\n* sind Führungskraft oder UnternehmerIn und mit Ihrem Team im Veränderungsprozess.\n""",
            """* möchten eine Veränderung in Ihrem Leben erwirken.""",
        ]

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
                                "background-color": card_color,
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
                                "background-color": card_color,
                            },
                            className="markdown-responsive align-content-center justify-content-center",
                        ),
                        justify="center",
                        className="align-content-center justify-content-center",
                        style={
                            "margin-top": "20px",
                            "margin-left": "-25px",
                            "background-color": card_color,
                        },
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
            """ \n \n Ich freue mich darauf, Sie bei einem unverbindlichen Erstgespräch näher kennen zu lernen!""",
            """ \n \n Ihre _Beatrice Koch_""",
        ]

    def markdown_text(self, text, weight="normal"):
        return dbc.Container(
            [
                dcc.Markdown(
                    text,
                    style={
                        "font-family": textfont["font-family"],
                        "line-height": "1.1",
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
        return self.path + "assets/yes-hand.png"

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
                        "margin-bottom": "20px",
                    },
                ),
                dmc.CardSection(
                    self.timeline(),
                    # py="xl",
                    style={
                        "align": "center",
                        "margin-bottom": "20px",
                        "margin-top": "40px",
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
        return """## Ablauf eines Coachings"""
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
                    "line-height": "1.1",
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
            """Jedes Anliegen ist so individuell wie ihrE TrägerIn. Daher biete ich keine vordefinierten Pakete an. Eine Sitzung dauert 50 oder 90min. Die Frequenz variiert je nach Anliegen. """,
        ]

    def _accordion_item3_text(self):
        return [
            """Eine Abschlusssitzung ist bei längeren Veränderungsphasen hilfreich. Wir reflektieren Ihre Entwicklungsschritte und gehen die Erkenntnisse der Sitzungen gemeinsam durch.""",
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
                            self._footer(),
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

    def _footer(self):
        return dbc.Button(
            children="Impressum",
            href="/impressum",
            className="mb-3",
            color=card_color,
            n_clicks=0,
        )

    def timeline(self):
        return dmc.Timeline(
            id="timeline",
            active=1,
            bulletSize=20,
            lineWidth=2,
            children=[
                self.timeline_item_with_button(
                    "Unverbindliches Erstgespräch",
                    self._accordion_grid(self.accordion_image1(), self.accordion_content(self._accordion_item1_text())),
                    timelineid="time1",
                    spoilerid="info1",
                ),
                self.timeline_item_with_button(
                    "Sitzungen",
                    self._accordion_grid(self.accordion_image2(), self.accordion_content(self._accordion_item2_text())),
                    timelineid="time2",
                    spoilerid="info2",
                ),
                self.timeline_item_with_button(
                    "Optionales Abschlussgespräch",
                    self._accordion_grid(self.accordion_image3(), self.accordion_content(self._accordion_item3_text())),
                    timelineid="time3",
                    spoilerid="info3",
                ),
                self.timeline_item_with_button(
                    "",
                    children="",
                    timelineid="time4",
                    spoilerid="info4",
                ),
            ],
        )

    def timeline_item(self, title, children, timelineid, spoilerid):
        return dmc.TimelineItem(
            title=self.markdown_text(title),
            children=[
                dmc.Text(
                    [
                        dmc.Spoiler(
                            showLabel="Show more",
                            hideLabel="Hide",
                            initialState=False,
                            maxHeight=0,
                            children=[children],
                            id=spoilerid,
                        ),
                    ],
                    color="dimmed",
                    # size="sm",
                ),
            ],
            id=timelineid,
            style={"font-family": headline["font-family"], "font-weight": "normal"},
        )

    def timeline_item_with_button(self, title, children, timelineid, spoilerid):
        return dmc.TimelineItem(
            title=self.markdown_text(title),
            children=[
                dbc.Button(
                    id=timelineid,
                    className="mb-3",
                    color=card_color,
                    n_clicks=0,
                ),
                dbc.Collapse(
                    dmc.Card(dmc.CardSection(children), style={"background-color": card_color}),
                    id=spoilerid,
                    is_open=False,
                    style={"background-color": card_color},
                ),
            ],
            id=timelineid,
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
                self.markdown_text("""## Referenzen""", weight="bold"),
                style={
                    "align": "center",
                    "background-color": card_color,
                    # "margin-top": "10px",
                    # "margin-bottom": "20px",
                },
            ),
            dbc.Row(
                dmc.Card(
                    self.ref_container(self._first_ref()[0], self._first_ref()[1]),
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
                    self.ref_container(self._second_ref()[0], self._second_ref()[1]),
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
                    self.ref_container(self._third_ref()[0], self._third_ref()[1]),
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

    def ref_container(self, text, cite):
        return dbc.Container(
            [
                dmc.Blockquote(
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        initialState=False,
                        maxHeight=63,
                        children=text,
                        id="ref1",
                    ),
                    cite=cite,
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

    def _first_ref(self) -> Tuple[str, str]:
        return (
            "Mit Beatrice findet man eine Begleitung fürs Leben. Durch ihre ruhige Art gibt sie Sicherheit. Sie schafft es, dem Klienten in seinem Anliegen zu folgen und gleichzeitig zu führen. Sie kann sehr gut zuhören und begleitet die eigene Entwicklung professionell und sehr klar. Die Anwendung vielfältiger Methoden hilft auch aus komplexen Situationen einen Ausweg zu finden. Ihre offen und unkomplizierte Art macht es einem sehr leicht sich zu öffnen und auch schwierige Dinge auszusprechen.",
            "- Annika",
        )

    def _second_ref(self) -> Tuple[str, str]:
        return (
            "Beatrice hat mir geholfen, mit einem liebevollen und urteilsfreien Blick auf meine Herausforderungen zu sehen. Während ich vor den gemeinsamen Coaching-Sessions wahnsinnig harsch über mich selbst geurteilt und mich ständig mit anderen Menschen verglichen habe, lösten die Gespräche mit Beatrice einen Perspektivwechsel in mir aus. Ihre Art, meine existierende Sichtweisen zu hinterfragen und alternative Szenarien und Interpretationen in den Raum zu stellen, lässt mich sowohl mich selbst, als auch die Welt um mich herum, offener betrachten. Gemeinsam haben wir Konzepte erarbeitet, die mir helfen, mit Selbstzweifeln und Perfektionismus kurzfristig umzugehen und langfristig bestehende Muster zu durchrechen.",
            "- Laura",
        )

    def _third_ref(self) -> Tuple[str, str]:
        return (
            """Über den Zeitraum von mehr als einem Jahr hat mich Beatrice im Rahmen von systemischen Coaching Sessions begleitet.
Mir war es im Rahmen der Sessions ein Anliegen, meine Kommunikation in professionellen Kontexten zu verbessern. Ihre Sessions waren dabei immer gut strukturiert und dennoch flexibel genug, um auf aktuelle Themen aus meinem Leben einzugehen. Durch gezielte Fragestellungen konnte ich mein Kommunikationsverhalten reflektieren, was sich direkt in meiner professionellen Kommunikation bemerkbar machte. Zudem legte mir Beatrice auch wertvolle Methoden nahe, die ich über unsere Sessions hinaus anwenden konnte.
Ein weiterer Schwerpunkt unserer Arbeit lag auf generellen Karriereentscheidungen. Beatrice half mir, meine beruflichen Ziele klarer zu definieren und konkrete Schritte zu planen, um diese zu erreichen. Ihre Methoden sind praxisnah und lösungsorientiert, was mir half, Unsicherheiten abzubauen und selbstbewusster Entscheidungen zu treffen.
Ich bin Beatrice ausgesprochen dankbar für die durchweg positive und bereichernde Erfahrung!""",
            "- Manuel",
        )
