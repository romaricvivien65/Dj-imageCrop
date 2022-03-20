"""imagecrop URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from images import views as public_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',public_views.main_view, name='U_home')
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
