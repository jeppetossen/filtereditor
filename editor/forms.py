from django.forms import ModelForm
from .models import ItemSettings


class ItemSettingsForm(ModelForm):
    class Meta:
        model = ItemSettings
        fields = ['section', 'block', 'show_hide', 'rarity', 'sound', 'icon', 'beam']
