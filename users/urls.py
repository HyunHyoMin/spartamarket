from django.contrib import admin
from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('<str:username>/profile', views.profile, name='profile'),
    path('<str:username>/update_profile', views.update_profile, name='update_profile'),
    path('<int:member_pk>/follow', views.follow, name="follow"),
    path('<str:member_username>/follower', views.follower, name="follower"),
    path('<str:member_username>/following', views.following, name="following"),
]
