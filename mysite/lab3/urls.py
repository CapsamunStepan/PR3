from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'lab3'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='lab3:home'), name='logout'),
    path('set_status/', views.set_status, name='set_status'),
]
