from editor.models import Block


def reset(key):
    settings = Block
    try:
        settings.objects.get(id=key).delete()
    except settings.DoesNotExist:
        return None


if __name__ == '__main__':
    pass
