from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.TopPage.as_view(), name='top'),
    path('show_list/', views.ShowList.as_view(), name='show_list'),
    #path('detail/<int:pk>/', views.ShowDetailView.as_view(), name='detail'),
    path('detail/', views.ShowDetailView.as_view(), name='detail'),
    path('week_with_schedule/', views.ShowList.as_view(), name='week_with_schedule'),

    path('new_week/', views.WeekView.as_view(), name='new_week'),
]
