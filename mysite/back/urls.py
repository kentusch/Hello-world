from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^mainpage/$', views.index, name='index')
]
