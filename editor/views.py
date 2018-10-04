from django.shortcuts import render
from django.views.generic import TemplateView

from editor.content import headers


# Create your views here.
def index(request):
    sections = headers.fetch_header()

    return render(request, "editor/index.html", {"sections": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
