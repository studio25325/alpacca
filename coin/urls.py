from django.contrib import admin
from django.urls import path

from . import views


from django.views.generic import TemplateView
from django.views.decorators.cache import cache_control


app_name = 'coin'

urlpatterns = [
    path('', views.index, name='index'),
    path('more', views.more),
    path('slack', views.slack),
]
