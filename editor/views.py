from django.shortcuts import render
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

    if (request.method == "POST") and (f"show_{number}" in request.POST):
        show = models.ItemSettings(id=number, show_hide="show")
        show.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"hide_{number}" in request.POST):
        hide = models.ItemSettings(id=number, show_hide="hide")
        hide.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"disable_{number}" in request.POST):
        disable = models.ItemSettings(id=number, show_hide="disable")
        disable.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"copy_{number}" in request.POST):
        pass
    elif (request.method == "POST") and (f"paste_{number}" in request.POST):
        pass
    elif (request.method == "POST") and (f"reset_{number}" in request.POST):
        settings.reset(number)
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"sound_{number}" in request.POST):
        sound = models.PlayAlertSound(id=number, sound_id=int(), volume=int())
        sound_apply = models.ItemSettings(id=number, sound=sound)
        sound_apply.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"icon_{number}" in request.POST):
        icon = models.MinimapIcon(id=number, size=int(), color="", shape="")
        icon_apply = models.ItemSettings(id=number, icon=icon)
        icon_apply.save()
        return HttpResponseRedirect('')
    elif (request.method == "POST") and (f"beam_{number}" in request.POST):
        beam = models.PlayEffect(id=number, color="", temp="")
        beam_apply = models.ItemSettings(id=number, beam=beam)
        beam_apply.save()
        return HttpResponseRedirect('')
    else:
        sections = headers.load_headers()
        return render(request, "editor/index.html", {"sections": sections})
