from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/update_comment/', views.update_comment, name='update_comment'),
    path('<int:pk>/like/', views.like, name="like"),
]
