from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from src.ui.bluetooth_panel import BluetoothPanel
from src.ui.audio_panel import AudioPanel
from src.ui.devices_panel import OutputDevicesPanel


class HyprAudio(App):
    CSS_PATH = "hypraudio_style.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield BluetoothPanel()
            with Vertical(classes="column"):
                yield AudioPanel()
                yield OutputDevicesPanel()


if __name__ == "__main__":
    app = HyprAudio()
    app.run()
