from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('room/<str:pk>/', views.room, name="room"),
    path('room/<str:pk>/createtopic/', views.createtopic, name="create-topic"),
    path('room/<str:pk>/topic/', views.topic, name="topic"),
    path('user/<str:pk>/', views.userProfile, name="user-profile"),
]