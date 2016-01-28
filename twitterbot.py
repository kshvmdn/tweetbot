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

    def respond(self, mention_text, message):
        for mention in self.api.mentions_timeline(count=1):
            if mention_text in mention.text.lower():
                self.tweet(message.format(mention.user.screen_name), mention.id)
                self.api.create_favorite(mention.id)
                print('Responded to {0}.'.format(mention.user.screen_name))

if __name__ == '__main__':
    tb = TwitterBot()
    tb.respond('hi', '{} hey buddy!')
