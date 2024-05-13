import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..utils.dash_base_template import DashBasePage

from dash import dcc
from dash import html

import logging


logger = logging.getLogger(__name__)


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
                "fontFamily": "'Inter', sans-serif",
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
                                # dbc.Col(
                                self._layout_body_card(),
                                # width={"size": 10, "offset": 0},
                                # class_name="mt-auto",
                                # ),
                            ],
                            class_name="mb-5",
                        ),
                    ],
                    fluid=True,
                )
            ],
        )

    def _layout_body_card(self):
        return dmc.Card(
            children=[
                dmc.CardSection(
                    children=[
                        dmc.SimpleGrid(
                            cols=3,
                            children=self._layout_cardheader_second_row(),
                            mt="sm",
                            breakpoints=[
                                {"minWidth": 1001, "maxWidth": 2000, "cols": 3},
                                {"minWidth": 600, "maxWidth": 1000, "cols": 1},
                            ],
                        ),
                    ],
                    withBorder=True,
                    inheritPadding=True,
                    mr=0,
                    style={"width": "100%", "backgroundcolor": "lightgray"},
                ),
                dmc.CardSection(self._layout_cardbody(), inheritPadding=True, withBorder=True),
                dmc.CardSection(self._layout_cardbody_third_row(), withBorder=True, inheritPadding=True),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            mr=0,
            style={"width": "100%", "backgroundcolor": "lightgray"},
        )

    def _layout_cardheader(self):
        return self._layout_cardheader_second_row()

    def _layout_cardheader_second_row(self):
        return [
            dmc.Image(
                radius="md",
                src=self.path + "assets/Website_Header.svg",
                style={"width": "100%", "height": "100%"},
                # height="180px",
            ),
            dmc.Image(
                radius="md",
                src=self.path + "assets/Unbenannt.png",
                fit="cover",
                style={"width": "100%", "height": "100%"},
            ),
            dmc.Card(
                [
                    dmc.CardSection(self._header_list(), inheritPadding=False, mr=0),
                    dmc.CardSection(
                        self._free_contact(),
                        py="xl",
                        style={"align": "center"},
                        inheritPadding=False,
                    ),
                ],
                style={"align": "center"},
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
        return self._carousel()  # dbc.Row([self._accordion()])

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
            ),
            size="auto",
        )

    def _header_list(self):
        return dcc.Markdown(
            "Sie \n* stehen Privat oder im Beruf vor einer Veränderung.\n* sind Führungskraft oder Unternehmer und mit ihrem Team im Veränderungsprozess.\n* möchten eine Veränderung in Ihrem Leben erwirken.",
            style={
                "font-family": "Georgia",
                "align": "left",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
                "margin-bottom": "-20px",
                "margin-top": "-20px",
                "margin-right": "-20px",
                "margin": "0px",
                "line-height": "1.1",
            },
            className="markdown-responsive",
        )

    def _free_contact(self):
        return html.Div(
            style={"display": "flex", "justifyContent": "center", "alignItems": "center", "margin-bottom": "20px"},
            children=[
                dmc.Anchor(
                    dmc.Button(
                        "Kostenfreies Erstgespräch",
                        variant="outline",
                        rightIcon=DashIconify(icon="ic:baseline-email"),
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
                dbc.Row(
                    dcc.Markdown(
                        """Ich coache, um Sie bei herausfordernden Situationen systemisch zu unterstützen.  \n  \n Gemeinsam betrachten wir Ihre Situation „von außen“. Mit dem damit gewonnenen Abstand erlangen Sie neue Perspektiven. Und damit einhergehend eine Erweiterung Ihrer Handlungs-, Denk- und Haltungsoptionen. \n  \n Häufig leiten uns Glaubenssätze, angelernte Verhaltens- und Denkmuster. Diese sind so tief verwurzelt, dass wir sie nicht hinterfragen. Genau hier setze ich an. Durch systemische Fragetechniken und Methoden fördere ich die Selbstreflektion. So finden wir „innere blinde Flecken“, die ihre Haltung und Handlung beeinflussen. Erst wenn diese sichtbar werden, haben Sie die Chance, den Umgang mit ihnen aktiv zu gestalten. \n \n Ich coache nach dem systemisch-konstruktivistischen Ansatz. Methoden aus verschiedenen Ansätzen, zum Beispiel aus der Gestaltung, finden bei mir Anwendung. Damit verfolge ich eine wissenschaftlich fundierte Herangehensweise im Coaching. \n \n Ich freue mich darauf, Sie bei einem unverbindlichen Kennenlerngespräch näher kennen zu lernen! \n \n Ihre Beatrice Koch""",
                        style={
                            "font-family": "Georgia",
                            "margin-bottom": "20px",
                            "margin-top": "20px",
                        },
                        className="markdown-responsive",
                    )
                ),
            ],
            fluid=True,
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
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(
                            "Ablauf eines Coachings",
                            icon=DashIconify(
                                icon="icon-park-solid:info",
                                color=dmc.theme.DEFAULT_COLORS["blue"][6],
                                width=20,
                            ),
                        ),
                        dmc.AccordionPanel(self._carousel()),
                    ],
                    value="info",
                ),
            ],
        )
