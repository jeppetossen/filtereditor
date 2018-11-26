from django.shortcuts import render
from django.views.generic import TemplateView

from editor.modules.headers import headers
from .models import ItemSettings


# Create your views here.
def index(request):
    header_keys = headers.retrieve_header_id()
    x = [k for k in header_keys]
    if (request.method == "POST") and ("show1" in request.POST):
        new_show = ItemSettings(id=1, show_hide="show")
        new_show.save()
    elif (request.method == "POST") and (f"hide{x}" in request.method):
        pass
    elif (request.method == "POST") and (f"copy{x}" in request.method):
        pass
    elif (request.method == "POST") and (f"paste{x}" in request.method):
        pass
    elif (request.method == "POST") and (f"reset{x}" in request.method):
        pass
    elif (request.method == "POST") and (f"sound{x}" in request.method):
        sound = request.POST.get('sound', '')
        # skapa
        new_item_settings = ItemSettings()
        new_item_settings.sound = sound
        # new_item_settings.block = "block here"
        new_item_settings.save()
        # editera
        '''item_settings = ItemSettings.objects.get(pk=settings_id)
        item_settings.sound = sound
        item_settings.block = "editerad block"
        item_settings.save()'''
    elif (request.method == "POST") and (f"icon{x}" in request.method):
        pass
    elif (request.method == "POST") and (f"beam{x}" in request.method):
        pass
    else:
        sections = headers.fetch_header()
        return render(request, "editor/index.html", {"headers": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
