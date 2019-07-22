from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.TopPage.as_view(), name='top'),
    #path('show_list/', views.ShowList.as_view(), name='show_list'),
    #path('detail/<int:pk>/', views.ShowDetailView.as_view(), name='detail'),
    #path('detail/', views.ShowDetailView.as_view(), name='detail'),
    #path('week_with_schedule/', views.ShowList.as_view(), name='week_with_schedule'),
    #以下、本番用
    path('', views.ScheduleView.as_view(), name='schedule'),
    path('create/', views.ScheduleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ScheduleUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.ScheduleDetailView.as_view(), name='detail'),
]
