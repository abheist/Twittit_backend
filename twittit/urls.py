from django.conf.urls import url
from django.urls import path

from twittit.views import TwitterLogin
from . import views

urlpatterns = [
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login')
]
