from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('mysnakes', views.mySnakes, name='mysnakes'),
    path('snake/<int:pk>/', views.snake_detail, name='snake_detail'),
    path('snake/add/', views.snake_add, name='snake_add'),
    path('snake/<int:pk>/edit/', views.snake_edit, name='snake_edit'),
]
