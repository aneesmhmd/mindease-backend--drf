from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admindj/', admin.site.urls),
    path('api/',include('accounts.urls')),
    path('admin/',include('admin_home.urls')),
    path('services/',include('home.urls')),
    path('counselor/',include('counselor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
