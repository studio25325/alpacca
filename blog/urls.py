from django.urls import path
from . import views

#画像表示用
from django.contrib.auth import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('<int:url_next_month>/', views.ScheduleView.as_view(), name='next'),
    path('<int:url_previous_month>/', views.ScheduleView.as_view(), name='previous'),

    path('create/', views.ScheduleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ScheduleUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.ScheduleDetailView.as_view(), name='detail'),
]

#画像表示用
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
