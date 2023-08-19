from django.urls import path
from app1 import views
from app1.views import SearchResaultsView, SelectedpostView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('categories/<str:selected_category>/', views.selected_category, name='selected_category'),
    path("search/", SearchResaultsView.as_view(), name="search_results"),
    path("articles/<int:article_id>/", SelectedpostView.as_view(), name="selected_post"),
]
