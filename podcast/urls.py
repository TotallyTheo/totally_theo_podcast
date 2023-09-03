from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('episodes/', views.episodes, name='episodes'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
