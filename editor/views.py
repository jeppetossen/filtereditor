from django.shortcuts import render
from django.http import HttpResponseRedirect

from editor.modules.headers import headers
from editor import models
# from .forms import ItemSettingsForm
from editor.modules.filterformat import settings


def index(request):
    sections = headers.load_headers()
    return render(request, "editor/index.html", {"sections": sections})
