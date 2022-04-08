from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
      path('login/', views.loginView,name="login"),
      path('logout/', views.logoutUser,name="logout"),
      path('register/', views.RegisterView,name="register"),


    
      path('', views.home, name = "home"),
      path('room/<str:pk>/', views.room, name = "room"),  
      path('create-room/', views.createRoom, name="create-room"),
      path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
      path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
       path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),


]