# package imports
import dash
from dash import html
from ..ui.layout import FrontEndLayout
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc


class Empty(FrontEndLayout):
    def __init__(self):
        super().__init__()
        self.path = ""
        # dash app layout definition
        self.layout = self.layout()
        # callback initializations
        self.button_state_callbacks = ""  # button_state_callbacks
        self.register_callbacks(self.app)

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
                                dbc.Col(
                                    self._layout_body_card(),
                                    width={"size": 10, "offset": 1},
                                    class_name="mb-4",
                                ),
                            ],
                            class_name="mb-5",
                        ),
                    ],
                    fluid=True,
                )
            ],
        )

    def _layout_body_card(self):
        return dbc.Card(
            children=[
                dbc.CardBody(children=self._empty_page_text()),
            ],
            color="ligth",
            outline=False,
            # style={"height": "80vh"},
        )

    def _empty_page_text(self):
        return dbc.Container(
            [
                dbc.Row(
                    dcc.Markdown(
                        """Leider existiert diese Seite noch nicht!""",
                        style={"font-family": "Georgia", "font-size": "3rem", "text-align": "center"},
                    )
                ),
            ],
            fluid=True,
        )
