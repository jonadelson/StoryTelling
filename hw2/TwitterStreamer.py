# Code partially adapted from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# This code uses 'apple fbi' as a keyword to examine tweets related to the current
# story on whether Apple should be forced to assist the government in unlocking the 
# iPhone that belonged to one of the San Bernardino shooters. 

import json
import time
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Credentials
API_KEY = '5mzm3qQTbpN82LYtdlC2iuMVE'
API_SECRET = 'KGuyr3RiiWh3DRYPiSUq1ia2anfXiq7SAzXXhJBdymq2R2dajK'
ACCESS_TOKEN = '3127328500-e6PNj8ltrqXBSfGkAR6LcYogFx1OSJYzX2Cxeic'
ACCESS_TOKEN_SECRET = 'x9QAzJ90gICvHi83YOa92ZOFVIpVJPJwveBIOeOE4Fp5p'

class StdOutListener(StreamListener):

    def on_data(self, data):
        """
        This function says what to do with the data when it is consumed
        in the stream. It prints out the text associated with the tweet 
        and the timestamp of the tweet. The timestamp will be used downstream
        in order to calculate the rate at which tweets are coming in and 
        try to determine whether some important event has occured
        """
        # Data comes in as JSON so we read it into a python dictionary
        decoded = json.loads(data)
        # Create a JSON object to print to stdout
        json_object = {'text':decoded['text'], 'time':decoded['timestamp_ms']} # object that will hold tweet info
        # print the object
        print json.dumps(json_object)
        # make sure that it gets flushed to stdout
        sys.stdout.flush()

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
    search_term = 'iphone fbi'

    # start stream and filter term 
    stream.filter(track=[search_term])
