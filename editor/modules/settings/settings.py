class Settings:

    def __init__(self, id_n, show_hide, copy=None, paste=None,
                 reset=None, sound=None, icon=None, beam=None):
        self.id_n = id_n
        self.show_hide = show_hide
        self.copy = copy
        self.paste = paste
        self.reset = reset
        self.sound = sound
        self.icon = icon
        self.beam = beam

    def item_id(self):
        pass

    def item_show_hide(self):
        pass

    def sound(self):
        pass

    def icon(self):
        pass

    def beam(self):
        pass


class Sound(Settings):

    def __init__(self, id_n, show_hide, sound):
        super().__init__(id_n, show_hide, sound)
        self.sound = sound

    def sound(self):
        pass
