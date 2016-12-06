import numpy as np
import twitter
from DatumBox import DatumBox
#import sklearn as sk
import string
import dAccessToken
import tAccessToken
import matplotlib.pyplot as plt
import unicodedata
import re
import tDataGatherer
import random

# dAccess = dAccessToken.dAccessToken()
# datum_box = DatumBox(dAccess.api_key)
# t = tDataGatherer.TDataGatherer()
# t.fetchStatuses('barackobama', 10)
# statuses = t.getFullStatuses() 
# tweets = t.getTweets(True, True)
# times = t.getTimes()

def getStrippedTweets(tweets, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags):
	newTweets = []
	for tweet in tweets:
		newTweets.append(stripString(tweet, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags))
	return newTweets

def stripString(s, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags):
	s = unicodedata.normalize('NFKD', s).encode('ascii','ignore')
	s = re.sub(r'[0-9]*', '', s, flags=re.MULTILINE)
	if (shouldStripURLs):
		s = re.sub(r'https?:\/\/.*[\r\n]*', '', s, flags=re.MULTILINE)
	if (shouldStripHashTags):
		s = re.sub(r'#[A-z]*', '', s, flags=re.MULTILINE)
	if (shouldStripUsers):
		s = re.sub(r'@[A-z]*', '', s, flags=re.MULTILINE)
	if (shouldStripPunct):
		exclude = set(string.punctuation)
		exclude.remove("'")
		s = ''.join(ch for ch in s if ch not in exclude)
	s = re.sub(r'RT', '', s, flags=re.MULTILINE)
	return s.lower()

def plottweetresults(tweetresults,username):
    #assuming I get the tweetresults in a list 
    #pie chart showing percentages of positive,neutral,negative
    positive = 0
    negative = 0
    neutral = 0
    for item in tweetresults:
        if item == 'positive':
            positive += 1
        elif item == 'negative':
            negative += 1
        else:
            neutral += 1
    sizes = [positive,negative,neutral]
    colors = ['blue','red','white']
    explode = (0,0,0)
    labels = 'Positive Tweets','Negative Tweets','Neutral Tweets'
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=140)
    plt.axis('equal')
    plt.title(str(username) + 'Tweet Analysis')
    plt.savefig("positivity.png")               

def getTweetTimesByTime(times):
        #get tweets per time of the day
	timeOfTweets = defaultdict(lambda:0)
	for time in times:
		timeOfTweets[time[2]] += 1
	times = range(24)
	numbers = []
	for time in times:
		numbers.append(timeOfTweets[time])
	return [times,numbers]


def gettweetsentiment(datumBox, tweets):
    #assuming I get tweets in a list format
    data = []
    for tweet in tweets:
        print tweet
        sentiment = datumBox.twitter_sentiment_analysis(tweet)
        data.append(sentiment)
    return data

