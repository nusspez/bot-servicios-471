from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API, Stream
from config import config

auth_config = config.get('auth')
auth = OAuthHandler(auth_config.get('consumer_key'), auth_config.get('consumer_secret'))
auth.set_access_token(auth_config.get('access_key'), auth_config.get('access_secret'))
client = API(auth)

accounts_to_follow = [d.get('id') for d in config.get('retweet').get('from')]

class Listener(StreamListener):
    def on_status(self, status):
        if status.author.id_str in accounts_to_follow:
            # client.retweet(status['id'])
            print(status.text)
    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
    stream_listener = Listener()
    stream = Stream(auth=client.auth, listener=stream_listener)
    stream.filter(follow=accounts_to_follow, async=True)
