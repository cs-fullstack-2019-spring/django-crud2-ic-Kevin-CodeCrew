from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users/edit/<int:id>/', views.edituser, name='edit'),
    path('users/delete/<int:id>/', views.deleteuser, name='delete'),


]