from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.ajax),
    path('more', views.TestView.more),
    path('', views.TestView.as_view(), name='test'),
]
