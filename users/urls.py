from django.contrib import admin
from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('update_profile/<str:username>', views.update_profile, name='update_profile'),
]
