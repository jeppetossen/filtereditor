from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from editor.modules.headers import headers
from editor import models
# from .forms import ItemSettingsForm
from editor.modules.filterformat import settings


# Create your views here.
def index(request):
    # header_keys = headers.retrieve_header_id()
    name = str()
    number = str()
    if request.method == "POST":
        for k in request.POST:
            name = k

        for i in name:
            if i.isdigit():
                number += str(i)

    if (request.method == "POST") and (f"show{number}" in request.POST):
        show = models.ItemSettings(id=number, show_hide="show")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"hide{number}" in request.POST):
        hide = models.ItemSettings(id=number, show_hide="hide")
        hide.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"copy{number}" in request.POST):
        pass
    elif (request.method == "POST") and (f"paste{number}" in request.POST):
        pass
    elif (request.method == "POST") and (f"reset{number}" in request.POST):
        settings.reset(number)
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"sound{number}" in request.POST):
        sound = models.PlayAlertSound(id=number, sound_id=int(), volume=int())
        sound_apply = models.ItemSettings(id=number, sound=sound)
        sound_apply.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"icon{number}" in request.POST):
        icon = models.MinimapIcon(id=number, size=int(), color="", shape="")
        icon_apply = models.ItemSettings(id=number, icon=icon)
        icon_apply.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"beam{number}" in request.POST):
        beam = models.PlayEffect(id=number, color="", temp="")
        beam_apply = models.ItemSettings(id=number, beam=beam)
        beam_apply.save()
        return HttpResponseRedirect('')
    else:
        subsections = headers.get_subsection_id()
        sections = headers.load_headers()
        return render(request, "editor/index.html", {"headings": sections,
                                                     "subsections": subsections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
