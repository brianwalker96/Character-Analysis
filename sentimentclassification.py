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

class sentimentClassifier:
    def __init__ (tweets):
        dAccess = dAccessToken.dAccessToken()
        self.datumBox = DatumBox(dAccess.api_key)
        self.tweets = tweets

def plotTweetResults(tweetresults):
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
    #plt.title(str(username) + 'Tweet Analysis')
    plt.savefig("positivity.png")               

# def getTweetTimesByTime(times):
#         #get tweets per time of the day
# 	timeOfTweets = defaultdict(lambda:0)
# 	for time in times:
# 		timeOfTweets[time[2]] += 1
# 	times = range(24)
# 	numbers = []
# 	for time in times:
# 		numbers.append(timeOfTweets[time])
# 	return [times,numbers]


def getTweetSentiment(datumBox, tweets):
    #assuming I get tweets in a list format
    data = []
    for tweet in tweets:
        # print tweet
        sentiment = datumBox.twitter_sentiment_analysis(tweet)
        data.append(sentiment)
    return data

