def set_border_color(red, green, blue, alpha=None):
    if alpha is not None:
        return "SetBorderColor {} {} {} {}".format(red, green, blue, alpha)
    else:
        return "SetBorderColor {} {} {}".format(red, green, blue)


def set_text_color(red, green, blue, alpha=None):
    if alpha is not None:
        return "SetTextColor {} {} {} {}".format(red, green, blue, alpha)
    else:
        return "SetTextColor {} {} {}".format(red, green, blue)


def set_background_color(red, green, blue, alpha=None):
    if alpha is not None:
        return "SetBackgroundColor {} {} {} {}".format(red, green, blue, alpha)
    else:
        return "SetBackgroundColor {} {} {}".format(red, green, blue)


def set_font_size(font_size=32):
    return "SetFontSize {}".format(font_size)


def play_alert_sound(sid, volume=None):
    if volume is not None:
        return "PlayAlertSound {} {}".format(sid, volume)
    else:
        return "PlayAlertSound {}".format(sid)


def play_alert_sound_positional(sid, volume=None):
    if volume is not None:
        return "PlayAlertSoundPositional {} {}".format(sid, volume)
    else:
        return "PlayAlertSound {}".format(sid)


def disable_drop_sound():
    return "DisableDropSound"


def custom_alert_sound(file=""):
    return "CustomAlertSound {}".format(file)


def minimap_icon(size, color, shape):
    return "MinimapIcon {} {} {}".format(size, color, shape)


def play_effect(color, temp=""):
    return "PlayEffect {} {}".format(color, temp)