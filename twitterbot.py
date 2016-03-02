import tweepy
import time


class TwitterBot:
    def __init__(self, twitter_auth, listen_list, response_msg):

        auth = tweepy.OAuthHandler(twitter_auth['consumer_key'],
                                   twitter_auth['consumer_secret'])
        auth.set_access_token(twitter_auth['access_token'],
                              twitter_auth['access_token_secret'])
        self.api = tweepy.API(auth)
        self.responded_tweets = []
        self.listen, self.response = listen_list, response_msg

    def tweet(self, message, mention_id=None):
        self.api.update_status(status=message, in_reply_to_status_id=mention_id)

    def reply_to_mention(self):
        print('  Searching mentions...')
        for mention in self.api.mentions_timeline():
            if any(t in mention.text.lower() for t in self.listen) \
                    and mention.id not in self.responded_tweets:
                print('   Found tweet - {}'.format(mention.text))
                try:
                    self.tweet(self.response.format(mention.user.screen_name),
                               mention.id)
                    self.api.create_favorite(mention.id)
                    print('    Responded to {}'.format(mention.user.screen_name))
                except tweepy.TweepError:
                    print('    Already responded')
                self.responded_tweets.append(mention.id)
                time.sleep(5)
