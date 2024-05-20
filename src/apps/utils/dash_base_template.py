import dash
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime, date
from abc import ABC, abstractmethod
import logging
import sys

logger = logging.getLogger(__name__)

weekdays = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag",
    6: "Samstag",
    7: "Sonntag",
}

months = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}


class DashBasePage:
    def __init__(self, **kwargs):
        # self.ENV = str(sys.argv[1])
        ## dash app definition
        from src.app import app

        self.app = app
        self._callbacks = []
        self.path = ""

    def layout(self):
        return html.Div(
            [
                dbc.Container(
                    [
                        dbc.Row(
                            [dbc.Col(html.H1(children="BASE LAYOUT"), width={"size": 7, "offset": 2}, className="mb-2")]
                        )
                    ]
                )
            ]
        )

    def register_components(self):
        """register subcomponents so that their callbacks will be registered

        Searches self.__dict__, finds all DashBaseCallbacks and adds them to self._callbacks
        """
        if not hasattr(self, "__callback"):
            self._callbacks = []
        for k, v in self.__dict__.items():
            if k != "_callbacks" and isinstance(v, DashBaseCallback) and v not in self._callbacks:
                self._callbacks.append(v)

    def register_callbacks(self, app):
        """First register all subcomponents, then call register_callbacks(app)"""
        self.register_components()
        print(f"components: {self._callbacks}")
        for callback in self._callbacks:
            if hasattr(callback, "register_callbacks"):
                callback.register_callbacks(app)


class DashBaseHandler:
    def __init__(self):
        return

    def _extract_year(self, date: date) -> int:
        return date.year

    def _extract_calendar_week(self, date: date) -> int:
        return int(date.strftime("%V"))

    def _extract_day_of_week(self, date: date) -> str:
        return weekdays[date.isoweekday()]

    def _extract_month(self, date: date) -> str:
        return months[date.month]

    def _parse_date(self, date_str: str) -> date:
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    def _log_trigger(self) -> str:
        functionNameAsString = sys._getframe(1).f_code.co_name
        changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
        logger.info(f"function: {functionNameAsString} triggered by: {changed_id}")
        return changed_id


class DashBaseCallback(ABC):
    def __init__(self):
        self.__callback = True

    @abstractmethod
    def register_callbacks(self):
        pass
