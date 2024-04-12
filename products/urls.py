from django.urls import path
from accounts import views

app_name = 'products'
urlpatterns = [
    path('detail/', views.detail, name='detail'),
]
