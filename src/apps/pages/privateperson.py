import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)
accordion_color = "#D6DCE5"  # "#F8F9FA"


class PrivatePerson(DashBasePage):
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
                            "justify-content": "end",
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
                src=self.path + "assets/privat.png",
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
                        """\n* Sie möchten in ihrem privaten Leben eine Veränderung erwirken, kommen aber nicht voran.""",
                        """\n* Sie sind ungewollt in ihrem privaten Umfeld einer Veränderung ausgesetzt, die Sie bewältigen müssen.""",
                        """\n* Sie sind bereits aktiv in einer Veränderungsphase und möchten dabei begleitet werden.""",
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
                        """Veränderungen begleiten unser gesamtes Leben. Es gibt von außen sichtbare Veränderungen, z.B. einen Umzug, einen Jobwechsel, oder das Zurückkommen ins Berufsleben nach einer Pause. Es gibt auch Veränderungen, die im Verborgenen stattfinden und unsere Haltung oder das Denken beeinflussen. Manchmal ist diese Veränderung von einem Erlebnis ausgelöst worden, auch wenn man es selbst nicht so richtig zuordnen kann. Und es gibt Veränderungen, die wir uns wünschen – z.B. im beruflichen Kontext mit Vorgesetzten und oder KollegInnen oder eine andere Work-Life Balance.""",
                        """ \n \n Veränderungen können also:""",
                        """ \n* „von innen“ motiviert – aber schwierig in der Umsetzung sein""",
                        """ \n* im eigenen Denken und Handeln passieren – und man weiß selbst gar nicht genau, wie es dazu kam""",
                        """ \n* uns ungewollt „passieren“ """,
                        """ \n* uns gewollt „passieren“ – und trotzdem herausfordernd sein""",
                        """ \n \n Egal welche Veränderung bei Ihnen passiert ist oder ansteht: ein systemisches Coaching hilft, die Veränderung zu verstehen, anzuerkennen und aktiv zu gestalten.""",
                        """ \n \n In den Coaching-Sessions schauen wir uns gemeinsam Ihre Situation an und analysieren, was genau Sie herausfordert. Ob, und wenn ja, welche Ängste oder Glaubenssätze zu Grunde liegen, die es Ihnen schwer machen, die Veränderung anzunehmen oder anzugehen. Im nächsten Schritt erörtern wir Handlungsoptionen, die Sie ohne Coaching vielleicht nicht gesehen hätten. Und Sie entscheiden schlussendlich, welchen Weg Sie gehen wollen.""",
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

    def _third_row(self):
        return [
            dmc.Card(
                [
                    dmc.CardSection(
                        self._third_card_text(),
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
                    # "width": "100%",
                    # "height": "100%",
                    "align-self": "center",
                    "background-color": "#D6DCE5",
                    "justify-content": "center",
                },
            ),
            dbc.Container(
                [
                    dmc.Image(
                        src=self.path + "assets/privat2.png",
                        # className="d-flex justify-content-end",
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
                ],
                fluid=True,
                className="d-flex justify-content-end",
                style={
                    # "margin-bottom": "20px",
                    # "margin-top": "20px",
                    "background-color": "#D6DCE5",
                    # "width": "100%",
                    # "height": "100%",
                    "align-self": "center",
                    "justify-content": "end",
                },
            ),
        ]

    def _third_card_text(self):
        return dbc.Container(
            [
                dcc.Markdown(
                    [
                        """Mit Privatpersonen sind nicht ausschließlich „private Themen“ gemeint. Es können selbstverständlich ebenso Fragestellungen aus dem beruflichen Kontext eingebracht werden.""",
                        """ \n „Privatpersonen“ dient hier lediglich zur Abgrenzung gegenüber Führungskräften und UnternehmerInnen, die mit ihrem Team eine Veränderungsphase anstreben bzw. durchleben und dabei professionelle Unterstützung wünschen.""",
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
