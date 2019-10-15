from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('twittit/', include('twittit.urls')),
    path('admin/', admin.site.urls),
]
