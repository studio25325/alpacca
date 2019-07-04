from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.TopPage.as_view(), name='top'),
    path('<int:pk>/', views.post10_detail, name='post10_detail'),
    path('new/', views.post10_new, name='post10_new'),
    path('<int:pk>/edit/', views.post10_edit, name='post10_edit'),
]
