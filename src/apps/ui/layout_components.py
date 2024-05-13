from dash import dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from .component_ids import ButtonIds, DropdownIds,  LayoutComponentIds
from dash_iconify import DashIconify
from dash import dcc
from dash import dash_table
from dash import html
from datetime import timedelta, date
import logging

logger = logging.getLogger(__name__)

PAGE_SIZE = 30


def interval_update_component(id: str):
    return dcc.Interval(
        id=id,
        max_intervals=-1,
        n_intervals=0,
        interval=1000 * 60 * 60 * 24,
    )

def notification_and_saving_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle(id=LayoutComponentIds.modal_title)),
            dbc.ModalBody(id=LayoutComponentIds.modal_body),
            dbc.ModalFooter([create_button(label ="Close", id=ButtonIds.close_modal_button, disabled=False)])
        ],
        id=LayoutComponentIds.notification_and_saving_modal,
        is_open=False,
    )

def upload_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle(["Upload Excel File"])),
            dbc.ModalBody([upload_component(id=LayoutComponentIds.upload_component),
                           datatable(id = LayoutComponentIds.datatable_in_modal, style_cell= {"fontSize": 12,"font-family": "sans-serif","height": "auto","textOverflow": "ellipsis",
                                                                                    "minWidth": "180px", "width": "180px", "maxWidth": "180px","whiteSpace": "normal"}),
                           html.Div(id='upload_modal_saving_feedback'),
                           html.H6("Uploaded files"),
                           html.Ul(id=LayoutComponentIds.uploaded_files_list),
                           html.H6("Download example"),
                           html.Ul(id=LayoutComponentIds.example_files_list)
                           ]),
            dbc.ModalFooter([create_button(label ="Save", id=ButtonIds.save_modal_button, disabled=True), 
                             create_button(label ="Delete uploaded Files", id=ButtonIds.delete_uploaded_files_button, disabled=True),
                             create_button(label ="Close", id=ButtonIds.close_upload_modal_button, disabled=False)
                             ])
        ],
        id=LayoutComponentIds.upload_modal,
        is_open=False,
        size = "lg"
    )

def create_button(label: str, id: str, disabled: bool):
    return dbc.Button(
        label,
        id=id,
        size='sm',
        n_clicks=0,
        disabled=disabled,
        outline=True,
        color="dark"
    )

def store(id: str):
    return dcc.Store(id=id, storage_type='session')

def datatable(id: str, style_cell: dict):
    return dash_table.DataTable(
        id=id,
        export_format=None,
        sort_action="custom",
        sort_mode="multi",
        sort_by=[],
        filter_action="custom",
        filter_query=(""),
        export_headers="display",
        editable=True,
        fixed_rows={"headers": True},
        dropdown={
            "Table": {
                "options": [
                    {"label": i, "value": i}
                    for i in [
                        "lrb_compressed_mod",
                        "ios_app_reporting",
                        "om_report",
                        "clicks_and_costs",
                        "salesforce_conversion_details",
                        "campaign_lookup",
                        "business_partner_lookup",
                    ]
                ]
            },
            "Acknowledged": {"options": [{"label": str(i), "value": i} for i in [True, False]]},
        },
        cell_selectable=True,
        page_current=0,
        page_size=PAGE_SIZE,
        page_action="custom",
        style_table={
            "overflowX": "auto",
            "height": "62vh",
            "maxHeight": "62vh",
            "overflowY": "auto",
            "minWidth": "100%",
            "position": "relative",
            "zIndex": 0,
        },
        style_header={
            "fontSize": 12,
            "font-family": "sans-serif",
            "backgroundColor": "white",
            "fontWeight": "bold",
            "position": "relative",
            "zIndex": 0,
        },
        style_cell=style_cell,
        style_data={
            "whiteSpace": "normal",
            "height": "auto",
            "lineHeight": "15px",
            "color": "black",
            "backgroundColor": "white",
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": ("rgb(220, 220, 220)"),
            },
            {
                "if": {"column_id": "ID"},
                "display": "None",
            },
            {
                "if": {
                    "filter_query": (
                        '{{{column}}} eq "{content}"'.format(
                            column="Date",
                            content="SUMME",
                        )
                    )
                },
                "fontWeight": "bold",
                "backgroundColor": ("rgb(250, 250, 250)"),
            },
        ],
        style_header_conditional=[
            {
                "if": {"column_id": "ID"},
                "display": "None",
            }
        ],
        style_filter_conditional=[
            {
                "if": {"column_id": "ID"},
                "display": "None",
            }
        ],
    )


def datepicker():
    return dmc.DateRangePicker(
        id=LayoutComponentIds.date_picker,
        icon=[DashIconify(icon="clarity:date-line")],

        minDate=date(2021, 7, 1),
        modalZIndex=99999,
        allowSingleDateInRange=True,
        zIndex=99999,
        dropdownType='modal',
        value=[date.today() - timedelta(days=2), date.today() - timedelta(days=1)],
        required=True,
        clearable=False,
        style={"width": 250},
        )

def table_dropdown(data: list):
    return dmc.Select(
        placeholder="Select a table",
        id=DropdownIds.table_dropdown,
        value=None,
        clearable=False,
        searchable=True,
        data=data,
        icon=DashIconify(icon="radix-icons:magnifying-glass"),
        style={'position': 'relative', 'zIndex': 900})

def column_dropdown():
    return dmc.MultiSelect(
            placeholder="Select columns",
            id=DropdownIds.column_dropdown,
            value=None,
            clearable=False,
            searchable=True,
            icon=DashIconify(icon="radix-icons:magnifying-glass"),
            style={'position': 'relative', 'zIndex': 900})

def notification_button_and_badge():
    return dbc.Button(
        [
            "Notifications",
            dbc.Badge(id=LayoutComponentIds.notification_badge,
                        text_color="secondary",
                        pill=True,
                        className="position-absolute top-0 start-100 translate-middle"),
        ],
        id=ButtonIds.notification_button,
        color="dark",
        outline=True,
        className="position-relative",
        size='sm'
    )

def button_with_tooltip(id: str, label: str, icon: str, tooltip: str):
    return dmc.Tooltip(
        dmc.Button(
            label,
            id=id,
            leftIcon=DashIconify(icon=icon),
            variant="outline",
            size='sm',
            n_clicks=0),
        label=tooltip,
        multiline=True,
        width=350,
        withArrow=True,
        transition="fade",
        transitionDuration=200,
        position='bottom'
    )

def import_button(button_id: str, link_id: str, name: str, title: str):
    return dmc.Tooltip(
        html.A(
        dmc.Button(
            name,
            id=button_id,
            leftIcon=DashIconify(icon="mdi:import"),
            variant="outline",
            n_clicks=0,
        ),
        href="/",
        id=link_id,
        target=("_blank"),
    ),
    label=(title),
    multiline=True,
    width=220,
    withArrow=True,
    transition="fade",
    transitionDuration=200,
    position='bottom')

def checkbox():
    return dmc.Chip(
        children="Show only changes",
        id=ButtonIds.only_changes_button,
    )

def alert(id: str):
    return dbc.Alert(id=id, is_open=False, color="warning", dismissable=True)

def toast(id: str):
    return dbc.Toast(
                html.P("Alert won't be shown again!", className="mb-0"),
                id=id,
                header="Alert acknowledged",
                icon="success",
                duration=2500,
                is_open=False,
                dismissable=True,
                style={
                    "position": "fixed",
                    "top": 46,
                    "right": 330,
                    "width": 450
                },
            )

def upload_component(id: str):
    return dcc.Upload(
                id=id,
                children=html.Div(
                    ["Drag and drop or click to select a file to upload."]
                ),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=True,
            )

def return_text_and_icon_as_feedback(text:str, color:str, icon:str):
        return dmc.Group(
                [   dmc.Text(text, weight=700, color=color),
                    dmc.ActionIcon(
                        DashIconify(icon=icon), color=color, variant='filled'
                    )
                ])
