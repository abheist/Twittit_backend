from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from twittit.views import TwitterLogin, MakeTweet

urlpatterns = [
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url('tweet/', MakeTweet.as_view(), name='make_tweet')
]

urlpatterns = format_suffix_patterns(urlpatterns)
