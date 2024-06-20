from django.urls import path, include
from django.contrib.auth import logout
from . import views

app_name = 'translation'
urlpatterns = [
    path('instant_translation/', views.instant, name='instant'),
    path('browse_projects/', views.browse, name='browse'),
    path('create_project/', views.create, name='create'),
    path('current_project/<int:id>/', views.PostUpdateView.as_view(), name='current'),
    path('test/<int:x>/', views.test, name='test'),


]


