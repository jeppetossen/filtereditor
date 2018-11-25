def item_level(value, operator=""):
    if operator is not None:
        return f"ItemLevel {operator} {value}"
    else:
        return f"ItemLevel {value}"


def drop_level(value, operator=""):
    if operator is not None:
        return f"ItemLevel {operator} {value}"
    else:
        return f"ItemLevel {value}"


def quality(value, operator=""):
    if operator is not None:
        return f"Quality {operator} {value}"
    else:
        return f"Quality {value}"


def rarity(value, operator=""):
    return f"Rarity {operator} {value}"


def item_class(i_class=""):
    return f"Class {i_class}"


def base_type(basetype):
    return f"BaseType {basetype}"


def sockets(value, operator=""):
    return f"Sockets {operator} {value}"


def linked_sockets(value, operator=""):
    return f"LinkedSockets {operator} {value}"


def socket_group(group=""):
    return f"SocketGroup {group}"


def height(value, operator=""):
    return f"Height {operator} {value}"


def width(value, operator=""):
    return f"Width {operator} {value}"


def has_explicit_mod(value):
    return f"HasExplicitMod {value}"


def stack_size(value, operator=""):
    return f"StackSize {operator} {value}"


def gem_level(value, operator=""):
    return f"GemLevel {operator} {value}"


def identified(boolean):
    return f"Identified {boolean}"


def corrupted(boolean):
    return f"Corrupted {boolean}"


def elder_item(boolean):
    return f"ElderItem {boolean}"


def shaper_item(boolean):
    return f"ShaperItem {boolean}"


def shaped_map(boolean):
    return f"ShapedMap {boolean}"


def map_tier(value, operator=""):
    return f"MapTier {operator} {value}"
