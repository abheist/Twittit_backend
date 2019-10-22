from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('twittit.urls')),
    path('admin/', admin.site.urls),
]
