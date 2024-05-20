from .pages.privateperson import PrivatePerson

# from apps.utils.om_report_ui.button_state_callbacks import ButtonStateCallbacks
# from apps.utils.om_report_ui.button_state_handler import ButtonStateFunctions
# from apps.utils.om_report_ui.modal_callbacks import ModalCallbacks

import os
import logging
import tempfile


# button_state_callbacks = ButtonStateCallbacks(button_handler=button_handler)
page = PrivatePerson()

layout = page.layout()
