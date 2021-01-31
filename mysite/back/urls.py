from django.contrib import admin
from django.conf.urls import url, include
from back import views

urlpatterns = [
    url(r'^back/', views.back, name='back')
]