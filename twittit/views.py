import twitter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from secrets import *


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class MakeTweet:
    twitter_api = twitter.Api(consumer_key=TWITTER_APP_KEY,
                              consumer_secret=TWITTER_APP_SECRET,
                              access_token_key=TWITTER_ACCESS_TOKEN,
                              access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
    status = twitter_api.PostUpdate("secrets sauce is coming soon!!!")
