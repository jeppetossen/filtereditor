from django.urls import path
from editor import views
from django.conf.urls import url, include
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.authtoken import views as drf_views


app_name = 'editor'
urlpatterns = [
    #path('api/auth/', drf_views.obtain_auth_token, name="home"),
    path('api/headers/', views.HeadersRequest.as_view()),
    url('api/', get_schema_view()),
    url('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url('api/auth/token/refresh/$', TokenRefreshView.as_view()),
]
