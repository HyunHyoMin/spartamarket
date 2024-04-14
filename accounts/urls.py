from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>/profile', views.profile, name='profile'),
    path('<int:pk>/update_profile_image', views.update_profile_image, name='update_profile_image')
]
