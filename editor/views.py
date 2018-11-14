from django.shortcuts import render
from django.views.generic import TemplateView

from editor.modules.content import headers
from .forms import ItemSettingsForm
from .models import ItemSettings


# Create your views here.
def index(request):
    if (request.method == "post") and ("sound" in request.POST):
        sound = request.POST.get('sound', '')
        # skapa
        new_item_settings = ItemSettings()
        new_item_settings.sound = sound
        new_item_settings.block = "block here"
        new_item_settings.save()
        # editera
        item_settings = ItemSettings.objects.get(pk=settings_id)
        item_settings.sound = sound
        item_settings.block = "editerad block"
        item_settings.save()

    else:
        sections = headers.fetch_header()
        return render(request, "editor/index.html", {"sections": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
