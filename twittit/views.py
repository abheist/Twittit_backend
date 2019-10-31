import twitter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from secrets import *


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class MakeTweet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        social_account = user.socialaccount_set.get()
        tokens = social_account.socialtoken_set.get()
        try:
            twitter_api = twitter.Api(consumer_key=TWITTER_APP_KEY,
                                      consumer_secret=TWITTER_APP_SECRET,
                                      access_token_key=tokens.token,
                                      access_token_secret=tokens.token_secret)
            tweet = twitter_api.PostUpdate(request.data['tweet'])
            return Response("tweet")
        except Exception as e:
            print("==========================")
            print(e)
            print("==========================")
