import tweepy
import time


class TwitterBot:
    def __init__(self, auth, listen, reply):
        auth = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
        auth.set_access_token(auth.access_token, auth.access_token_secret)
        self.api = tweepy.API(auth)
        self.replies, self.reply, self.listen = ([], reply,
                                                 [t.lower() for t in listen])

    def tweet(self, msg, mention_id=None):
        self.api.update_status(status=msg, in_reply_to_status_id=mention_id)

    def reply_to_mention(self):
        print('  Searching mentions...')
        for mention in self.api.mentions_timeline():
            if any(t in mention.text.lower() for t in self.listen) \
                    and mention.id not in self.replies:
                print('   Found mention - {}'.format(mention.text))
                try:
                    self.tweet(self.reply.format(mention.user.screen_name),
                               mention.id)
                    self.api.create_favorite(mention.id)
                    print('    Replied to {}'.format(mention.user.screen_name))
                    time.sleep(5)  # wait 5 seconds if reply tweet was sent
                except tweepy.TweepError:
                    print('    Already replied')
                self.responded_tweets.append(mention.id)
            else:
                print('   No mentions found')
