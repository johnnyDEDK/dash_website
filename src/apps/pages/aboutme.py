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


class AboutMe(FrontEndLayout):
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
                                    image="assets/IMG_0569.jpg",
                                    text_content=self._header_list(text1=[""], text2=self.header_text_2()),
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
            self._layout_cardbody_first_row(),
            self._layout_cardbody_second_row(),
        ]

    def _layout_cardbody_first_row(self):
        return dbc.Row([self._main_text()])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._free_contact()])

    def header_text_2(self):
        return [
            """\n* Meine Stärke ist es, Menschen und Teams bei Ihrer Weiterentwicklung zu unterstützen.""",
            """\n* Mich motiviert die Veränderung – daher arbeite ich gerne in einem Umfeld, das bestehende Strukturen herausfordert.""",
            """\n* Meine ehrliche Neugier lässt mich Fragen stellen, die Sie bei Ihrer Reflektion unterstützen.""",
        ]

    def _main_text(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Über mich:""",
                        """ \n* Geboren und aufgewachsen in Freiburg im Breisgau.""",
                        """ \n* Studium der (internationalen) Betriebswirtschaftslehre in Nürnberg, Kolumbien und Passau.""",
                        """ \n* Aufnahme in einem Nachwuchsförderprogramm eines DAX-Konzerns in 2016. Seitdem habe ich mich in den Bereichen Digitales Produktmanagement und Kommunikation spezialisiert. In den vergangenen Jahren habe ich häufig international gearbeitet (China, USA, Südafrika) und Führungs- und Projektverantwortung übernommen.""",
                        """ \n* Bereits während meines Studiums habe ich mich viel mit dem Thema verantwortungsvolles Führen beschäftigt, z.B. im Rahmen des Stipendiums der Bayerischen EliteAkademie und Teilnahme der Sommerakademie Führung und Persönlichkeit.""",
                        """ \n* 2023 Beginn der Systemischen Coaching Ausbildung bei artop, Institut an der Humboldt-Universität zu Berlin, Abschluss April 2024.""",
                        """ \n _Die Ausbildung ist von Deutschlands führendem Coaching-Verband DBVC anerkannt und existiert seit 2001. Zudem besitzt **artop** den Status Educational Provider for Business Coaching des IOBC, einer in Deutschland registrierten internationalen Organisation für professionelles Coaching mit dem Fokus auf Business Coaching und Leadership._""",
                        """ \n* Hobbies: Wandern, Gleitschirmfliegen, Kochen, Backen, Lesen""",
                        """ \n \n Ich freue mich über ein unverbindliches Kennenlerngespräch mit Ihnen! \n \n""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "line-height": "1.1",
                        "margin-bottom": "20px",
                        "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "center",
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
