from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from editor.modules.headers import headers
from .models import ItemSettings
from .forms import ItemSettingsForm


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
        show = ItemSettings(id=number, show_hide="show")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"hide{number}" in request.method):
        hide = ItemSettings(id=number, show_hide="hide")
        hide.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"copy{number}" in request.method):
        pass
    elif (request.method == "POST") and (f"paste{number}" in request.method):
        pass
    elif (request.method == "POST") and (f"reset{number}" in request.method):
        pass
    elif (request.method == "POST") and (f"sound{number}" in request.method):
        show = ItemSettings(id=number, sound="")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"icon{number}" in request.method):
        show = ItemSettings(id=number, icon="")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"beam{number}" in request.method):
        show = ItemSettings(id=number, beam="")
        show.save()
        return HttpResponseRedirect('')
    else:
        sections = headers.fetch_header()
        return render(request, "editor/index.html", {"headers": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
