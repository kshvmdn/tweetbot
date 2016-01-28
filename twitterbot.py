import tweepy
import time


class TwitterBot:
    def __init__(self, auth, listen_msg, response_msg):
        auth = tweepy.OAuthHandler(auth['consumer_key'], auth['consumer_secret'])
        auth.set_access_token(auth['access_token'], auth['access_token_secret'])
        self.api = tweepy.API(auth)
        self.responded_tweets = set()
        self.listen, self.response = listen_msg, response_msg

    def tweet(self, message, mention_id=None):
        self.api.update_status(status=message, in_reply_to_status_id=mention_id)

    def respond_to_mention(self):
        print('  Searching mentions...')
        for mention in self.api.mentions_timeline():
            if self.listen in mention.text.lower() and mention.id not in self.responded_tweets:
                print('    Found tweet - {}'.format(mention.text))
                try:
                    self.tweet(self.response.format(mention.user.screen_name), mention.id)
                    self.api.create_favorite(mention.id)
                    print('      Responded to {}'.format(mention.user.screen_name))
                except tweepy.TweepError:
                    print('      Already responded')
                self.responded_tweets.add(mention.id)
                time.sleep(5)

if __name__ == '__main__':
    tb = TwitterBot()
    tb.respond('hi', '{} hey buddy!')
