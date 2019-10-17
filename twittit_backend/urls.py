from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('twittit/', include('twittit.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
