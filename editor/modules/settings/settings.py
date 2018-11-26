from editor.models import ItemSettings


class Settings:

    def __init__(self, id_n=int(), show_hide=str(), copy=None, paste=None,
                 reset=None, sound=None, icon=None, beam=None):

        self.settings = ItemSettings()
        self.settings.id_n = id_n
        self.settings.show_hide = show_hide
        self.settings.copy = copy
        self.settings.paste = paste
        self.settings.reset = reset
        self.settings.sound = sound
        self.settings.icon = icon
        self.settings.beam = beam

    def item_id(self):
        pass

    def item_show_hide(self):
        pass

    def item_sound(self):
        pass

    def item_icon(self):
        pass

    def item_beam(self):
        pass


class ItemId(Settings):

    def __init__(self, id_n):
        super().__init__(id_n=id_n)
        self.id_n = id_n


class ItemShowHide(Settings):

    def __init__(self, show_hide):
        super().__init__(show_hide=show_hide)
        self.show_hide = show_hide


class ItemCopy(Settings):

    def __init__(self, copy):
        super().__init__(copy=copy)
        self.copy = copy


class ItemPaste(Settings):

    def __init__(self, paste):
        super().__init__(paste=paste)
        self.paste = paste


class ItemReset(Settings):

    def __init__(self, reset):
        super().__init__(reset=reset)
        self.reset = reset


class ItemSound(Settings):

    def __init__(self, sound):
        super().__init__(sound=sound)
        self.sound = sound


class ItemIcon(Settings):

    def __init__(self, icon):
        super().__init__(icon=icon)
        self.icon = icon


class ItemBeam(Settings):

    def __init__(self, beam):
        super().__init__(beam=beam)
        self.beam = beam
