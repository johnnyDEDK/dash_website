import logging
from ..ui.layout import FrontEndLayout

logger = logging.getLogger(__name__)


class LandingPage(FrontEndLayout):
    def __init__(self):
        super().__init__()
        self.path = ""
        # dash app layout definition
        self.layout = self.layout()
        # callback initializations
        self.button_state_callbacks = ""  # button_state_callbacks
        self.register_callbacks(self.app)
