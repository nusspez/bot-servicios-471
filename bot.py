import os
import sys
from config import config

from tweepy import API, OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy.error import TweepError

auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

client = API(auth)

accounts_to_follow = [d.get('id') for d in config.get('retweet').get('from')]


class Listener(StreamListener):
    
    def on_status(self, status):
        retweet = False
        if status.author.id_str in accounts_to_follow and status.in_reply_to_user_id is None:
            retweet = True
            print(u'{1} (https://twitter.com/{0}/status/{2}) - @{0}'.format(
                status.user.screen_name,
                status.text[:20] + '...' if len(status.text) > 10 else status.text,
                status.id_str
            ))
        
        if retweet and '-d' not in sys.argv:
            try:
                client.retweet(status.id_str)
            except TweepError:
                pass
    
    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    stream_listener = Listener()
    stream = Stream(auth=client.auth, listener=stream_listener)
    stream.filter(follow=accounts_to_follow, async=True)
