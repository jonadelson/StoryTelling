# This program performs several functions. 
# It first establishes a connection to a redis database where we will
# store the JSON objects as they come in from the stream. We store them
# in a redis list data structure.
# Second, it uses praw, which is a python wrapper to the Reddit API
# Our way of displaying the tweets will be to submit a comment to a thread
# every time we believe we have detected an interesting event. 
# The comment that is submitted is simply the text of the last tweet that 
# was found in the moving average that is below a particular threshold. 
# It is possible that this tweet is not actually that relevant to the increase
# in Twitter data flow, but we hope that it is. 

import sys
import redis
import json
import praw

# connect to redis database
conn = redis.Redis()

# establish a connection to Reddit
r = praw.Reddit('Add tweets as comments to a thread')
# login to reddit so that we can leave comments
# normally the following line is uncommented, but I want to hide my password
# because it is a password I use for a lot of things
# r.login(username='StreamingData', password='XXXXXXX')
# Get the thread object that we will use to leave comments when stream picks up
thread = r.get_submission(url='https://www.reddit.com/r/test/comments/47d8ao/apple_iphone_fbi_case/')

# initialize a count variable that will tell us when to 
# calculate a moving average
count = 0
while True:
	# read JSON from stdin
	line = sys.stdin.readline()
	# load it as Python object
	d = json.loads(line)
	# Get the delta associated with object
	delta = d['delta']
	# add the delta to the end of the tweet
	conn.rpush('tweets', delta)
	# increment count each time we get new tweet
	count += 1
	# allow program to collect some tweets before we start
	# calculating moving averages
	if count < 20:
		continue

	# we want some space in between calculating the moving average
	# by using mod 10, this means that each subsequent average we 
	# calculate will share 10 values with the previous average
	# because we take 20 items from our list later
	if count % 10 == 0:
		# get the latest 20 items from the redis list data structure
		deltas = conn.lrange('tweets', count - 20, count)
		# convert them to floats because they are currently strings
		deltas = [float(diff) for diff in deltas]
		# get the average of the deltas
		avg = sum(deltas) / float(len(deltas))
		# print the average value
		print avg
		# I noticed that tweets would sometimes come in as bursts
		# Typically the value will be around .1 in the moving average
		# when they come in as bursts. I somewhat arbitrarily choose
		# 0.5 as my cutoff for what defines an interesting stream
		if avg < 0.5:
			# print the text associated with the last tweet to the command line
			print d['text']
			# Normally the following line would be uncommented
			# The next line adds a the latest tweet as a comment to the thread 
			# I set up
			# thread.add_comment(d['text'])
		# flush to make sure output gets printed
		sys.stdout.flush()



