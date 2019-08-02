from django.urls import path
from . import views

#画像表示用
from django.contrib.auth import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'schedule'

urlpatterns = [
    #以下、本番用
    path('', views.CalView.as_view(), name='schedule'),
    path('<int:get_next_year>/<int:get_next_month>/', views.CalView.as_view(), name='next_m'),
    path('move/<int:url_next_month>/', views.ScheduleView.as_view(), name='next'),

    path('<int:url_previous_month>/', views.ScheduleView.as_view(), name='previous'),

    path('create/', views.ScheduleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ScheduleUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.ScheduleDetailView.as_view(), name='detail'),

    #複数変数の受け渡し方
    path('test/', views.TestView.as_view(), name='test'),
    path('test/<int:set1>/<int:set2>/', views.TestView.as_view(), name='test2'),

]

#画像表示用
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
