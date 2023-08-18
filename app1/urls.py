from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:selected_category>/', views.selected_category, name='selected_category'),
]
