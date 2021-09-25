from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('know', views.know, name="know"),



]