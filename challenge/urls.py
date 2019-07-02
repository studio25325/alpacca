from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.TopPage.as_view(), name='top'),
    path('<int:pk>/', views.post10_detail, name='post10_detail'),
    path('new/', views.post10_new, name='post10_new'),
    path('<int:pk>/edit/', views.post10_edit, name='post10_edit'),

    #path('Post10Detail', views.Post10Detail.as_view(), name='post10_detail'),
]

#以下テンプレートビューのurlサンプル
#path('', views.Top.as_view(), name='top'),
#path('error/', views.ErrorPage.as_view(), name='error'),
#path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
