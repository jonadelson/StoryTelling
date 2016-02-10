# StoryTelling

Required library: tweepy

---------------------------------------------------------------------------

Note: Use port=8080 for websocketd because that is what index.html looks for

Usage:
websocketd --port=8080 python TwitterStreamer.py
python -m SimpleHTTPServer 8000
localhost:8000

Wait a few seconds and the images and tweets should start to appear

----------------------------------------------------------------------------

In this exercise I will be consuming tweets from the Twitter Streaming API. 
I used this website (http://adilmoujahid.com/posts/2014/07/twitter-analytics/)
as a resource to understand how to consume tweets through the tweepy library 
in python. I experimented with a number of different search terms and ultimately
decided to use 'Isis' as my query. 

I focused only on the tweets that had a 'media_url_https' field associated with
them. Each individual message can represent a number of things. It can be a report
on a current news event related to Isis. It can be one of the presidential candidates
proclaiming they will fight terrorism and therefore invoking the name 'Isis'. I have 
found that often it can even be a joke from someone saying that someone else's actions
are even worse than Isis. 

I expect that there will be a lot of tweets associated with this. There probably
would have been more a few weeks ago, but it is still very much a hot topic and there
are still plenty of news stories concerning Isis as well as presidential candidates
invoking their name. The tweets come in fairly quickly so I make sure that I only print
the tweets after I have collected 10 with images so that the images and text associated
with a particular tweet remain on the webpage for long enough. 