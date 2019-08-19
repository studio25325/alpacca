from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'menu'


urlpatterns = [
    #path('', views.ajax),
    path('', views.MainView.as_view(), name='main'),
    #Ajax呼び出し先URL
    path('more', views.MainView.more),
    #データ編集用URL
    path('update/<int:pk>/', views.MenuUpdateView.as_view(), name='update'),
]
