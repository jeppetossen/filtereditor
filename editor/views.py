from django.shortcuts import render
from django.views.generic import TemplateView

from editor.modules.content import headers
from .forms import ItemSettingsForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ItemSettingsForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
    else:
        sections = headers.fetch_header()
        return render(request, "editor/index.html", {"sections": sections})


class ThemePageView(TemplateView):
    template_name = "editor/theme.html"


class SettingsPageView(TemplateView):
    template_name = "editor/settings.html"


class AboutPageView(TemplateView):
    template_name = "editor/about.html"
