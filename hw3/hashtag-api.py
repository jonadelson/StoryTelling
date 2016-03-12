# This program builds an API to make probability
# queries about hashtags associated with tweets
# about ISIS

import flask
from flask import request
import redis
from collections import Counter
import json
import numpy as np

# create a flask application
app = flask.Flask(__name__)
# establish connection to redis
conn = redis.Redis()

# helper function that returns the probabilities 
# associated with all of the tweets
def buildHistogram():
	# get all of the keys (these are timestamps)
	keys = conn.keys()
	# get the values (hashtags) associated with timestamps
	values = conn.mget(keys)
	# count how many times each hashtag has occured
	c = Counter(values)
	# get the normalizing constant to calculate probabilities
	z = sum(c.values())
	# return a dictionary of hashtag to probabilities
	return {k:v/float(z) for k,v in c.iteritems()}

# root directory will return the probabilities associated
# with each hashtag. They are returned in order from most 
# common to least common by probability
@app.route("/")
def histogram():
	# first get the probabilities
	h = buildHistogram()
	# get the probabilities as a list now so that 
	# we can sort by how common the term is
	h_items = h.items()
	# get the sorted probabilities
	sorted_items = sorted(h_items, key = lambda x:-x[1])
	# start building a string that will be displayed
	out = ""
	# add the hashtag and probability associated with the
	# hashtag to the string
	for item in sorted_items:
		out += str(item[0]) + " " + str(item[1]) + "<br/>"
	return out

# the /entropy url calculates the entropy
# of the distribution
@app.route("/entropy")
def entropy():
	# get all of the probabilities
	h = buildHistogram()
	# return the entropy of the distribution
	# which is given by a particular formula
	return json.dumps(-sum([p*np.log(p) for p in h.values()]))

# the /probability url returns the probability associated
# with any particular hashtag
# The most common hashtag when I was experimenting was "ISIS"
# So if you type "/probability?hashtag=ISIS", the page will return
# the probability associated with this hashtag
# If the hashtag does not appear, it returns a probability of 0
@app.route("/probability")
def probability():
	# get the hashtag that was requested
	hash_tag = request.args.get('hashtag', '')
	# get all of the probabilities, from which we will
	# choose the probability associated with the hashtag
	h = buildHistogram()
	# if the hashtag has not been encountered we return 
	# a probability of 0
	if hash_tag not in h:
		return json.dumps({
			"hash-tag": hash_tag,
			"probability": 0
			})
	# otherwise return the probability of the hashtag
	return json.dumps({
		"hash-tag": hash_tag,
		"probability": h[hash_tag]
		})

# run the actual server
if __name__ == "__main__":
	app.debug = True
	app.run()