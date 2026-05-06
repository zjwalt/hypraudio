import subprocess

class BluetoothController:
    def _run(self, command):
        result = subprocess.run(
            ['bluetoothctl'] + command,
            capture_output = True,
            text = True
        )
        return result.stdout

    def get_devices(self):
        result = self._run(['devices'])
        devices = []
        for line in result.strip().splitlines():
            parts = line.split(' ', 2)
            if len(parts) == 3 and parts[0] == 'Device':
                mac = parts[1]
                name = parts[2]
                if len(mac.split(':')) == 6 and not name.startswith(mac.replace(':', '-')):
                    devices.append({ 'mac': mac, 'name': name })

        return devices

    def is_connected(self, mac):
        output = self._run(['info', mac])
        return "Connected: yes" in output

    def trust(self, mac):
        self._run(['trust', mac])

    def connect(self, mac):
        self.trust(mac)
        self._run(['connect', mac])

    def disconnect(self, mac):
        self._run(['disconnect', mac])

    def scan(self, timeout=15):
        result = subprocess.run(
            ['bluetoothctl', '--timeout', str(timeout), 'scan', 'on'],
            capture_output=True,
            text=True
        )
        return self.get_devices()

