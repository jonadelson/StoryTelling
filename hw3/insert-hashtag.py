# This program reads a list of hashtags from standard in 
# and inserts each individual hashtag into a Redis database
# using the time that the hashtag was collected as the key

import json
import sys
import redis
import time

# establish database connection
conn = redis.Redis()

# loop forever
while True:
	# read the list of hashtags from standard in
	line = sys.stdin.readline()
	# throw into a try loop to avoid potential errors
	try:
		# load as a Python list
		decoded = json.loads(line)
	
		# This for loop will be skipped if the list is empty
		for hash_tag in decoded:
			# establish key for Redis database
			t = str(time.time())
			# put hashtag in database, expire after 5 minutes
			conn.setex(t, hash_tag, 300)
			# print for potential debugging
			print hash_tag
			# make sure it is actually output
			sys.stdout.flush()
	except:
		pass