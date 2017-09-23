from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API, Stream
from config import config
import os

auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

client = API(auth)

accounts_to_follow = [d.get('id') for d in config.get('retweet').get('from')]


class Listener(StreamListener):
    
    def on_status(self, status):
        if status.author.id_str in accounts_to_follow and status.in_reply_to_user_id is None:
            # client.retweet(status['id'])
            print(status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    stream_listener = Listener()
    stream = Stream(auth=client.auth, listener=stream_listener)
    stream.filter(follow=accounts_to_follow, async=True)
