# This code is essentially the same as the code written by Mike Dewar
# in the class demonstration. It will receive JSON objects that are being
# piped in from the TwitterStreamer.py program. The program then calculates
# the difference (delta) of when the last tweet came in so that we can 
# get a sense of the overall rate at which tweets are arriving

import json
import sys

# initialize the last variable
last = 0

while True:
	# read JSON from stdin
	line = sys.stdin.readline()
	# load JSON into Python object
	d = json.loads(line)
	# time is a string so we must convert it to an int
	time = int(d['time'])
	# we will simply continue if it is the first object that we read
	# because we have nothing to compare it to yet in order to calculate
	# a delta
	if last == 0:
		last = time
		continue
	# delta is the time difference between two tweets
	# we divide by 1000 because it is measured in milliseconds
	delta = float(time - last) / 1000
	# we then print out a JSON object that will be used later 
	# to calculate a moving average of time differences
	print json.dumps({'text':d['text'], 'time':time, 'delta':delta})
	# flush to make sure that it actually prints every time
	sys.stdout.flush()
	# update the last variable so we properly calculate future deltas
	last = time