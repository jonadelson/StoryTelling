How to run the code:

1) redis-server (start the redis server)

2) python TwitterStreamer.py | python insert-hashtag.py

3) python hashtag-api.py

By default, Flask seems to run things on the localhost:5000 but check what the output of the program says to see which webpage to go to. 

localhost:5000/ will return the probabilities associated with a hashtag about Isis. All of the values in the database expire after 3 minutes, so the probabilities capture some time element as well. 

localhost:5000/entropy will return the entropy of the distribution

localhost:5000/probability?hashtag='<hashtag>' will return the probability associated with that particular hashtag