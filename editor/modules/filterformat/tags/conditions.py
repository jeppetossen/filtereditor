def item_level(value, operator=""):
    if operator is not None:
        return "ItemLevel {} {}".format(operator, value)
    else:
        return "ItemLevel {}".format(value)


def drop_level(value, operator=""):
    if operator is not None:
        return "ItemLevel {} {}".format(operator, value)
    else:
        return "ItemLevel {}".format(value)


def quality(value, operator=""):
    if operator is not None:
        return "Quality {} {}".format(operator, value)
    else:
        return "Quality {} {}".format(value)


def rarity(value, operator=""):
    return "Rarity {} {}".format(operator, value)


def item_class(i_class=""):
    return "Class {}".format(i_class)


def base_type(basetype):
    return "BaseType {}".format(basetype)


def sockets(value, operator=""):
    return "Sockets {} {}".format(operator, value)


def linked_sockets(value, operator=""):
    return "LinkedSockets {} {}".format(operator, value)


def socket_group(group=""):
    return "SocketGroup {}".format(group)


def height(value, operator=""):
    return "Height {} {}".format(operator, value)


def width(value, operator=""):
    return "Width {} {}".format(operator, value)


def has_explicit_mod(value):
    return "HasExplicitMod".format(value)


def stack_size(value, operator=""):
    return "StackSize {} {}".format(operator, value)


def gem_level(value, operator=""):
    return "GemLevel {} {}".format(operator, value)


def identified(boolean):
    return "Identified {}".format(boolean)


def corrupted(boolean):
    return "Corrupted {}".format(boolean)


def elder_item(boolean):
    return "ElderItem {}".format(boolean)


def shaper_item(boolean):
    return "ShaperItem {}".format(boolean)


def shaped_map(boolean):
    return "ShapedMap {}".format(boolean)


def map_tier(value, operator=""):
    return "MapTier {} {}".format(operator, value)
