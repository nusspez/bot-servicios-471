import tweepy

CONSUMER_KEY = 'tWO7XoirfPqQo8RdeYM8SvwbD'
CONSUMER_SECRET = '9T503l9pKTaZPu3j40Nd1Hpew1YXlgqvPqHuVVRUYPSkZephCT'
ACCESS_KEY = '911451685058379776-Ei9QMSQgBhhJrAn955RSdH90BtEnC4z'
ACCESS_SECRET = 'K12iw5WDAas2Dp57oEUXaObQVL4fEGt3YPiiusZLfGlF1'

with open('sources/retweets') as f:
    lines = f.readlines()
accounts_to_track = [x.strip() for x in lines]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = Listener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(follow=accounts_to_track, async=True)
