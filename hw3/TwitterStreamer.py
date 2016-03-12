# Code partially adapted from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# This code uses 'Isis' as a keyword to examine tweets related to the terrorist
# organization. The code extracts the hashtags and prints them to standard out

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
        in the stream. It prints out the hashtags that are associated
        with a tweet. If there are no hashtags, it will simply print 
        an empty list
        """
        # Put code in try loop to avoid potential errors
        try:
            # Read JSON data into python dictionary
            decoded = json.loads(data)
            # Get hashtags if there are any
            hash_tags = decoded['entities']['hashtags']
            # We want just the text of the hashtags
            hash_tags = [entity["text"] for entity in hash_tags]
            # print the list of hashtags
            print json.dumps(hash_tags)
            # make sure that it gets flushed to stdout
            sys.stdout.flush()
        except:
            pass

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
