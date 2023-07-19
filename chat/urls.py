from django.contrib import admin
from django.urls import path
from . import views
from chat.views import JobsPageView

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
    path('room/<str:pk>/',  views.room, name="room"),
    path('profile/<str:pk>/',  views.userProfile, name="profile"),

    path('create-room/',  views.CreateRoom, name="create-room"),
    path('update-room/<str:pk>/',  views.UpdateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.DeleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update_user/', views.updateuser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('jobs/', JobsPageView.as_view(), name="jobs"),
]
