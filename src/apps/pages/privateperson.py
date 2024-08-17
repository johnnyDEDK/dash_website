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


class PrivatePerson(FrontEndLayout):
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
                                    image="assets/privat.png",
                                    text_content=self._header_list(text1=[""], text2=self._header_text_2()),
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
                                    "align-self": "top",
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
                            "align-self": "top",
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
            self._layout_cardbody_first_row(),
            self._layout_cardbody_second_row(),
            self._layout_cardbody_third_row(),
            self._layout_cardbody_fourth_row(),
        ]

    def _layout_cardbody_first_row(self):
        return dbc.Row([self._main_text_1()])

    def _layout_cardbody_second_row(self):
        return dbc.Row([self._main_text_2()])

    def _layout_cardbody_third_row(self):
        return dbc.Row([self._main_text_3()])

    def _layout_cardbody_fourth_row(self):
        return dbc.Row([self._free_contact()])

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
            """\n* Sie möchten in ihrem Leben eine Veränderung erwirken, kommen aber nicht voran.""",
            """\n* Sie sind ungewollt in ihrem Umfeld einer Veränderung ausgesetzt, die Sie bewältigen müssen.""",
            """\n* Sie sind bereits aktiv in einer Veränderungsphase und möchten dabei begleitet werden.""",
        ]

    def _main_text_1(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Veränderungen begleiten unser gesamtes Leben. Es gibt von außen sichtbare Veränderungen, z.B. einen Umzug, einen Jobwechsel, oder das Zurückkommen ins Berufsleben nach einer Pause. Es gibt auch Veränderungen, die im Verborgenen stattfinden und unsere Haltung oder das Denken beeinflussen. Manchmal ist diese Veränderung von einem Erlebnis ausgelöst worden, auch wenn man es selbst nicht so richtig zuordnen kann. Und es gibt Veränderungen, die wir uns wünschen – z.B. im beruflichen Kontext mit Vorgesetzten und oder KollegInnen oder eine andere Work-Life Balance.""",
                        """ \n \n Veränderungen können also:""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "line-height": "1.1",
                        "margin-bottom": "-20px",
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

    def _main_text_2(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """ \n* „von innen“ motiviert – aber schwierig in der Umsetzung sein""",
                        """ \n* im eigenen Denken und Handeln passieren – und man weiß selbst gar nicht genau, wie es dazu kam""",
                        """ \n* uns ungewollt „passieren“ """,
                        """ \n* uns gewollt „passieren“ – und trotzdem herausfordernd sein""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "line-height": "1.1",
                        "margin-bottom": "0px",
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

    def _main_text_3(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """ \n \n Egal welche Veränderung bei Ihnen passiert ist oder ansteht: ein systemisches Coaching hilft, die Veränderung zu verstehen, anzuerkennen und aktiv zu gestalten.""",
                        """ \n \n In den Coaching-Sessions schauen wir uns gemeinsam Ihre Situation an und analysieren, was genau Sie herausfordert. Ob, und wenn ja, welche Ängste oder Glaubenssätze zu Grunde liegen, die es Ihnen schwer machen, die Veränderung anzunehmen oder anzugehen. Im nächsten Schritt erörtern wir Handlungsoptionen, die Sie ohne Coaching vielleicht nicht gesehen hätten. Und Sie entscheiden schlussendlich, welchen Weg Sie gehen wollen.""",
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

    def _third_row(self):
        return [
            dmc.Card(
                [
                    dmc.CardSection(
                        self._third_card_text(),
                        inheritPadding=True,
                        className="d-flex justify-content-center align-content-top",
                        style={
                            "align": "center",
                            "background-color": card_color,
                            "margin-top": "20px",
                            "align-self": "top",
                        },
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
                    # "width": "100%",
                    # "height": "100%",
                    "align-self": "top",
                    "background-color": card_color,
                    "justify-content": "center",
                },
            ),
            dmc.Image(
                src=self.path + "assets/privat2.png",
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
            [
                dcc.Markdown(
                    [
                        """Mit Privatpersonen sind nicht ausschließlich „private Themen“ gemeint. Es können selbstverständlich ebenso Fragestellungen aus dem beruflichen Kontext eingebracht werden.""",
                        """ \n „Privatpersonen“ dient hier lediglich zur Abgrenzung gegenüber Führungskräften und UnternehmerInnen.""",
                    ],
                    style={
                        "font-family": textfont["font-family"],
                        "line-height": "1.1",
                        "margin-bottom": "20px",
                        "margin-top": "20px",
                        "background-color": card_color,
                        "align-self": "top",
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
                "align-self": "top",
            },
        )
