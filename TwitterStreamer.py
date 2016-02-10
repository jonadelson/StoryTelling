import json
import sys
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from collections import Counter

API_KEY = '5mzm3qQTbpN82LYtdlC2iuMVE'
API_SECRET = 'KGuyr3RiiWh3DRYPiSUq1ia2anfXiq7SAzXXhJBdymq2R2dajK'
ACCESS_TOKEN = '3127328500-e6PNj8ltrqXBSfGkAR6LcYogFx1OSJYzX2Cxeic'
ACCESS_TOKEN_SECRET = 'x9QAzJ90gICvHi83YOa92ZOFVIpVJPJwveBIOeOE4Fp5p'

class StdOutListener(StreamListener):

    def __init__(self):
        self.out = []
        self.count = 0
    
    def on_data(self, data):
        decoded = json.loads(data)
        json_object = {}
        if 'media' in decoded['entities']:
            self.count += 1
            json_object['url'] = decoded['entities']['media'][0]['media_url_https']
            json_object['text'] = decoded['text']
            self.out.append(json_object)
            if self.count == 3:
                print json.dumps(self.out[:3])
                sys.stdout.flush()
                self.out = []
                self.count = 0
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)
    search_term = 'isis'

    stream.filter(track=[search_term])
