import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
accordion_color = "#D6DCE5"  # "#F8F9FA"


class AboutMe(DashBasePage):
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
                src=self.path + "assets/aboutme.png",
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
        return dbc.Row([self._main_text()])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._free_contact()])

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
                        """\n* Meine Stärke ist es, Menschen und Teams bei Ihrer Weiterentwicklung zu unterstützen.""",
                        """\n* Mich motiviert die Veränderung – daher arbeite ich gerne in einem Umfeld, das bestehende Strukturen herausfordert.""",
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

    def _main_text(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Über mich:""",
                        """ \n* Geboren und aufgewachsen in Freiburg im Breisgau""",
                        """ \n* Studium der (internationalen) Betriebswirtschaftslehre in Nürnberg, Kolumbien und Passau""",
                        """ \n* Aufnahme in einem Nachwuchsförderprogramm eines DAX-Konzerns in 2016. Seitdem habe ich mich in den Bereichen Digitales Produktmanagement und Kommunikation spezialisiert. In den vergangenen Jahren habe ich häufig international gearbeitet (China, USA, Südafrika) und Führungs- und Projektverantwortung übernommen.""",
                        """ \n* Bereits während meines Studiums habe ich mich viel mit dem Thema verantwortungsvolles Führen beschäftigt, z.B. im Rahmen des Stipendiums der Bayerischen EliteAkademie und Teilnahme der Sommerakademie Führung und Persönlichkeit""",
                        """ \n* 2023 Beginn der Systemischen Coaching Ausbildung bei artop, Institut an der Humboldt-Universität zu Berlin, Abschluss April 2024.""",
                        """ \n _Die Ausbildung ist von Deutschlands führendem Coaching-Verband DBVC anerkannt und existiert seit 2001. Zudem besitzt **artop** den Status Educational Provider for Business Coaching des IOBC, einer in Deutschland registrierten internationalen Organisation für professionelles Coaching mit dem Fokus auf Business Coaching und Leadership._""",
                        """ \n* Hobbies: Menschen weiterentwickeln, Wandern, Gleitschirmfliegen, Kochen, Backen, Lesen""",
                        """ \n \n Ich freue mich über ein unverbindliches Kennenlerngespräch mit Ihnen! \n \n""",
                    ],
                    style={
                        "font-family": "Georgia",
                        "margin-bottom": "20px",
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
