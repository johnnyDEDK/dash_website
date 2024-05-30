import dash
import dash_bootstrap_components as dbc

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
FONT_KARLA = "https://fonts.googleapis.com/css2?family=Karla:ital,wght@0,200..800;1,200..800&family=Spectral:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,200;1,300;1,400;1,500;1,600;1,700;1,800&display=swap"
external_stylesheets = ["assets/bootstrap.css", "assets/styles.css", FONT_KARLA]  # , dbc.themes.YETI, FONT_AWESOME

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
