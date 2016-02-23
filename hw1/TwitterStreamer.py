# Code partially adapted from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

import json
import time
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from collections import Counter

# Credentials
API_KEY = '5mzm3qQTbpN82LYtdlC2iuMVE'
API_SECRET = 'KGuyr3RiiWh3DRYPiSUq1ia2anfXiq7SAzXXhJBdymq2R2dajK'
ACCESS_TOKEN = '3127328500-e6PNj8ltrqXBSfGkAR6LcYogFx1OSJYzX2Cxeic'
ACCESS_TOKEN_SECRET = 'x9QAzJ90gICvHi83YOa92ZOFVIpVJPJwveBIOeOE4Fp5p'

class StdOutListener(StreamListener):

    def __init__(self):
        self.out = [] # keep list of JSON objects
        self.count = 0 # keep count of tweets that have images attached
    
    def on_data(self, data):
        """
        This function says what to do with the data when it is consumed
        in the stream. I decided to only print out tweets that had a 
        media_url_https field so there is a check for this particular field.
        Also, I wait until I have a list of 10 tweets before I print it out. 
        I wait for 10 tweets because I do not want the web page refreshing too often.
        I only send the first three tweets however because it is a bit overwhelming
        to actually look at 10 tweets at once on the webpage. 
        """
        decoded = json.loads(data)
        json_object = {} # object that will hold tweet info
        # Do a try clause because sometimes there is no entities field and 
        # we do not want this to crash our program
        try:
            # Check if there is a media field in entities
            if 'media' in decoded['entities']:
                self.count += 1
                # Collect the image url and the tweet text and add to the list
                json_object['url'] = decoded['entities']['media'][0]['media_url_https']
                json_object['text'] = decoded['text']
                self.out.append(json_object)
                # If there are 10 tweets, print them 
                if self.count == 10:
                    print json.dumps(self.out[:3])
                    sys.stdout.flush()
                    self.out = []
                    self.count = 0
        except:
            pass
        return True

    def on_error(self, status):
        """
        This function simply prints the error message if one happens to occur
        """
        print status


if __name__ == '__main__':

    l = StdOutListener() # instantiate class
    # Set up authorizations
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # set up the stream
    stream = Stream(auth, l)

    # keyword of term to search for
    search_term = 'isis'

    # start stream and filter term 
    stream.filter(track=[search_term])
