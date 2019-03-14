from django.forms import ModelForm
from .models import Block


class BlockForm(ModelForm):
    class Meta:
        model = Block
        fields = ['section', 'block', 'show_hide', 'rarity', 'sound', 'icon', 'beam']
