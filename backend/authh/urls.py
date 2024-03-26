
from django.urls import path, include
from django.contrib.auth import logout
from . import views
# Application name to avoid conflicts if link names are similar
app_name = 'authh'


urlpatterns = [
    # ready links from django
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='register'),
    path('edit/', views.edit, name='edit'),
    path('Logout/',views.logout_user, name='Logout'),
    

]