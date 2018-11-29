from editor.models import ItemSettings


def reset(key):
    settings = ItemSettings
    try:
        settings.objects.get(id=key).delete()
    except settings.DoesNotExist:
        return None


if __name__ == '__main__':
    pass
