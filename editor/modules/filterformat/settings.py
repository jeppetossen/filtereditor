from editor.models.filter_data import FilterBlock


def reset(key):
    settings = FilterBlock
    try:
        settings.objects.get(id=key).delete()
    except settings.DoesNotExist:
        return None


if __name__ == '__main__':
    pass
