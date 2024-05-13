import dash
import dash_bootstrap_components as dbc

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
external_stylesheets = ["assets/bootstrap.css", "assets/styles.css"]  # , dbc.themes.YETI, FONT_AWESOME

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    # meta_tags=[
    #     {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    # ],
)
app.config.suppress_callback_exceptions = True
app.title = "Veränderungen annehmen, angehen und gestalten."
server = app.server
