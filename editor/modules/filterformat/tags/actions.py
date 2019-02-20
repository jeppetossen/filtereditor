def set_border_color(red, green, blue, alpha=None):
    if alpha is not None:
        return f"SetBorderColor {red} {green} {blue} {alpha}"
    else:
        return f"SetBorderColor {red} {green} {blue}"


def set_text_color(red, green, blue, alpha=None):
    if alpha is not None:
        return f"SetTextColor {red} {green} {blue} {alpha}"
    else:
        return f"SetTextColor {red} {green} {blue}"


def set_background_color(red, green, blue, alpha=None):
    if alpha is not None:
        return f"SetBackgroundColor {red} {green} {blue} {alpha}"
    else:
        return f"SetBackgroundColor {red} {green} {blue}"


def set_font_size(font_size=32):
    return f"SetFontSize {font_size}"


def play_alert_sound(sid, volume=None):
    if volume is not None:
        return f"PlayAlertSound {sid} {volume}"
    else:
        return f"PlayAlertSound {sid}"


def play_alert_sound_positional(sid, volume=None):
    if volume is not None:
        return f"PlayAlertSoundPositional {sid} {volume}"
    else:
        return f"PlayAlertSound {sid}"


def disable_drop_sound():
    return "DisableDropSound"


def custom_alert_sound(file=""):
    return f"CustomAlertSound {file}"


def minimap_icon(size, color, shape):
    return f"MinimapIcon {size} {color} {shape}"


def play_effect(color, temp=""):
    return f"PlayEffect {color} {temp}"
