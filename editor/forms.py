from django.forms import ModelForm
from .models import ItemSettings


class ItemSettingsForm(ModelForm):
    class Meta:
        model = ItemSettings
        fields = ['section', 'block', 'showhide', 'rarity', 'sound', 'icon', 'beam']
