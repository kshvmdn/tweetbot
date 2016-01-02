import tweepy
import pprint
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

mentions = api.mentions_timeline(count=1)

for mention in mentions:
    if 'test' in mention.text:
        print(mention.user.screen_name)
