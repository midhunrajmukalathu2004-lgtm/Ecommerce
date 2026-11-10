from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('register/',views.register),
    path('user_home/',views.user_home),
    path('userprofile/',views.userprofile),
    path('products/',views.user_home),
    path('admin_home/',views.admin_home),
    path('user_edit/',views.user_edit),
    path('manage_user/',views.manage_user),
    path('delete_user/<int:id>/', views.delete_user),
    
    
]