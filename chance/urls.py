from django.urls import path
from . import views

#画像表示用
from django.contrib.auth import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'chance'

urlpatterns = [
    #以下、本番用
    path('', views.MainView.as_view(), name='chance'),
    path('new_match', views.MatchCreateView.as_view(), name='new_match'),
    path('match_view', views.MatchView.as_view(), name='match_view'),
    path('match_detail/<int:pk>/', views.MatchDetailView.as_view(), name='match_detail'),

    #path('', views.index, name='index'),

]
