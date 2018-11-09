from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from editor.modules.content import headers
from .forms import ItemSettingsForm
from .models import ItemSettings


# Create your views here.
def index(request):
    if (request.method == "post") and ("sound" in request.POST):
        pass
    else:
        sections = headers.fetch_header()
        return render(request, "editor/index.html", {"sections": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
