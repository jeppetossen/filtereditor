from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from editor.modules.headers import headers
from .models import ItemSettings
from .forms import ItemSettingsForm


# Create your views here.
def index(request):
    header_keys = headers.retrieve_header_id()
    shows = list()
    for i in header_keys:
        shows.append(f"show{i}")
    for show in shows:
        continue
    if (request.method == "POST") and (show in request.POST):
        print(show)
        print(request.POST)
        show = ItemSettings(id=1, show_hide="show")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and ("hide" in request.method):
        pass
    elif (request.method == "POST") and ("copy" in request.method):
        pass
    elif (request.method == "POST") and ("paste" in request.method):
        pass
    elif (request.method == "POST") and ("reset" in request.method):
        pass
    elif (request.method == "POST") and ("sound" in request.method):
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
    elif (request.method == "POST") and ("icon" in request.method):
        pass
    elif (request.method == "POST") and ("beam" in request.method):
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
