from django.urls import path

from . import views


app_name = 'editor'
urlpatterns = [
    path('', views.index, name="home"),
]
