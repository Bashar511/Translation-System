from django.urls import path, include
from django.contrib.auth import logout
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.index, name='dashboard'),
    path('Logout/',views.logout_user, name='Logout'),
    

]