from django.urls import path

from . import views

app_name = 'collect'

urlpatterns = [
    path('', views.index, name='index'),
    path('kabuka/', views.kabuka, name='index'),
    #path('', views.CollectView.as_view(), name='collect'),
]
