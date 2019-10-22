from django.conf.urls import url

from twittit.views import TwitterLogin

urlpatterns = [
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login')
]