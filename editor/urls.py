from django.urls import path

from . import views


app_name = 'editor'
urlpatterns = [
    path('home/', views.index, name="home"),
    path('theme/', views.ThemePageView.as_view(), name="theme"),
    path('settings/', views.SettingsPageView.as_view(), name="settings"),
    path('about/', views.AboutPageView.as_view(), name="about"),
]
