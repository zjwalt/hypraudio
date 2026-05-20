from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static, ListView, ListItem, Label
from src.bluetooth.bluetooth_controller import BluetoothController


class DeviceItem(ListItem):
    def __init__(self, name: str, mac: str, connected: bool):
        super().__init__()
        self.device_name = name
        self.mac = mac
        self.connected = connected

    def compose(self) -> ComposeResult:
        symbol = "●" if self.connected else "○"
        yield Label(f"[#e3bdff]{symbol}[/#e3bdff] {self.device_name}", markup=True)


class BluetoothPanel(Widget):
    BORDER_TITLE = "Bluetooth Devices"

    def compose(self) -> ComposeResult:
        yield ListView()

    def on_mount(self) -> None:
        self.bt = BluetoothController()
        self.load_devices()

    def on_key(self, event) -> None:
        list_view = self.query_one(ListView)
        if event.key == "j":
            list_view.action_cursor_down()
        elif event.key == "k":
            list_view.action_cursor_up()
        elif event.key == "d":
            item = list_view.highlighted_child
            with open("/tmp/debug.txt", "w") as f:
                f.write(str(item.classes))

    def load_devices(self) -> None:
        list_view = self.query_one(ListView)
        list_view.clear()
        devices = self.bt.get_devices()
        for device in devices:
            connected = self.bt.is_connected(device["mac"])
            list_view.append(DeviceItem(device["name"], device["mac"], connected))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item = event.item
        if isinstance(item, DeviceItem):
            if item.connected:
                self.bt.disconnect(item.mac)
                item.connected = False
            else:
                self.bt.connect(item.mac)
                item.connected = True
            self.load_devices()
