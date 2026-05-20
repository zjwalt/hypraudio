from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static, ListView, ListItem, Label


class OutputDevicesPanel(Widget):
    BORDER_TITLE = "Output Devices"

    def compose(self) -> ComposeResult:
        yield ListView()
