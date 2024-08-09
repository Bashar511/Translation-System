from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authh import views
from translationSite import views as v

urlpatterns = [
    path("",views.welcome,name="welcome" ),
    path("home/",views.HOME,name="home" ),
    path('about/',v.ABOUTUS, name="ABOUTUS"),
    path('contact/',v.CONTACTUS, name="CONTACTUS"),
    path("home/", include("translationSite.urls",namespace='translation')),
    path("auth/", include("authh.urls",namespace='authh')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

