import pulsectl

class AudioController:
    def __init__(self):
        self.pulse = pulsectl.Pulse("hpyraudio")

    def get_sinks(self):
        return self.pulse.sink_list()

    def get_default_sink(self):
        default_name = self.pulse.server_info().default_sink_name
        sinks = self.get_sinks()
        for sink in sinks:
            if sink.name == default_name:
                return sink
        return None

    def set_default_sink(self, sink):
        self.pulse.sink_default_set(sink)

    def set_volume(self, sink, volume):
        self.pulse.volume_set_all_chans(sink, volume)

    def set_mute(self, sink):
        self.pulse.mute(sink, not sink.mute)

