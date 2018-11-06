from django import forms
from .models import FilterSettings


class FilterSettingsForm(forms.ModelForm):
    class Meta:
        model = FilterSettings
        fields = ["section", "block", "sound", "icon", "beam"]
