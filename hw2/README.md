Program Usage:

> redis-server

> python TwitterStreamer.py | python diff.py | python calculate.py

Dependencies:

praw (Python wrapper for Reddit API)

tweepy (Python wrapper for Twitter API)

This will print the stream rate to stdout. The program I had originally was writing "interesting"
tweets as comments to a reddit thread, but I commented out that ability in the latest program
because my Reddit password is basically the one I use for everything important (I know, bad idea). 

The updated program that does not write to Reddit instead just writes the Tweet also to the command
line. 

Here is a link to the Reddit thread I created: 

https://www.reddit.com/r/test/comments/47d8ao/apple_iphone_fbi_case/

For some reason, I can only currently see the comments when I am signed in to Reddit so I have
also included a screenshot of what the thread looks like. 

------------------------------------------------------------------------------------------------

The following is a summary of Apple's battle with the FBI over accessing data from the 
iPhone belonging to one of the San Bernardino shooters. I will summarize the summary that 
can be found at the following website:
http://www.wired.com/2016/02/apples-fbi-battle-is-complicated-heres-whats-really-going-on/

Apple was given a court order to assist the government in obtaining data on an iPhone that belonged
to one of the San Bernardino shooters. The FBI wants Apple to install a specific type of software 
into Apple phones that would assist the FBI in getting access to its customers' data. 

The phone that belonged to the San Bernardino shooter has a passcode that cannot be unlocked
by brutforced guessing because the phone will permanently lock if the FBI exceeds a certain
number of guesses. Additionally, it is possible that this particular phone has an auto-erasure
feature that kicks in and destroys all of the data on the phone if the number of guesses is
exceeded. 

Apple has other security measures in place, such as a limit of 80 milliseconds in terms of how
long the system waits before it confirms that a password is correct or incorrect. This seems
like a very short period of time but is actually prohibitively long. For example, a six-digit 
password could take up to five years of guessing before being cracked by brute force. 

The San Bernardino shooter had an iPhone 5. If it had been an older phone, Apple would have 
the ability to obtain the phone's data without knowing the password but has added more security
features in the new operating systems. 

Apple does not actually have the ability to crack into the phone. The government would like to 
have access to a weaker version of Apple's system that does not support auto-erasure of the data
and does not have time delays when brute force guessing of the password is applied. 

Even if Apple allows this weaker form of software that the FBI can access, the FBI will still need
to use brute force guessing to unlock phones, which can be prohibitively expensive. However, many
are concerned that this presents a slippery slope for the future. 

Tim Cook, Apple's CEO, has been strongly outspoken against the measures that the government is taking. 
Other high-profile figures in the technology industry have also opined in the issue, including Mark
Zuckerberg, who is siding with Apple, and Bill Gates, who appears to have mixed feelings about the
issue. 

Privacy from the government has been a major issue on people's minds in recent history, especially
since June of 2013 when Edward Snowden released information about spying activities by the NSA, and 
this particular case has definitely brought these issues back into the public eye.  