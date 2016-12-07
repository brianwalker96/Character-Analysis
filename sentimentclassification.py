import twitter
from DatumBox import DatumBox
import string
import dAccessToken
import tAccessToken
import re
dAccess = dAccessToken.dAccessToken()
datum_box = DatumBox(dAccess.api_key)
from plotly import plotly
import plotly.plotly as plotly
import plotly.tools as tls
tls.set_credentials_file(username='abhious', api_key='1Tdwg7pmZUvqlMJhNEgD')
plotly.sign_in(username='abhious',api_key='1Tdwg7pmZUvqlMJhNEgD')
import tDataGatherer
import plotly.graph_objs as go
import random

class sentimentClassifier:
    def __init__ (tweets):
        dAccess = dAccessToken.dAccessToken()
        self.datumBox = DatumBox(dAccess.api_key)
        self.tweets = tweets

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
    fig = { 'data':[{'labels': ['Positive','Negative','Neutral'], 'values': [positive, negative, neutral], 'type':'pie', 'marker': {'colors':['rgb(56,75,126)','rgb(18,36,37)','rgb(34,53,101)']},}], 'layout':{'title':str(username) + ' Positivity Analysis'}}
    plotly.plot(fig)
                   

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

    def getsenttweet(tweets):
    #gives you a list of lists where first element is the topic and the second is the tweet for every tweet
    #should not be in the class, should be in different class
    data = []
    for tweet in tweets:
        topic = datum_box.topic_classification(tweet)
        data.append([topic,tweet])
    return data

    def happinesstimes(tweets,times):
    #assuming input of stripped tweets and times, plots tweet history over time 
    tweettimes = zip(tweets,times)
    months = {'Jan':{'positive':0,'negative':0,'neutral':0},'Feb':{'positive':0,'negative':0,'neutral':0},'Mar':{'positive':0,'negative':0,'neutral':0},
              'Apr':{'positive':0,'negative':0,'neutral':0},'May':{'positive':0,'negative':0,'neutral':0}, 'Jun':{'positive':0,'negative':0,'neutral':0},
              'Jul':{'positive':0,'negative':0,'neutral':0}, 'Aug':{'positive':0,'negative':0,'neutral':0}, 'Sep':{'positive':0,'negative':0,'neutral':0},
              'Oct':{'positive':0,'negative':0,'neutral':0}, 'Nov':{'positive':0,'negative':0,'neutral':0}, 'Dec':{'positive':0,'negative':0,'neutral':0}}
    for tweet,time in tweettimes:
        sentiment = datum_box.twitter_sentiment_analysis(tweet)
        month = time[3]
        months[month][sentiment] += 1
    pos = {}
    neg = {}
    neu = {}
    m = months.keys()
    for month in m:
        pos[month] = months[month]['positive']
        neg[month] = months[month]['negative']
        neu[month] = months[month]['neutral']
    p = []
    n = []
    nu = []
    x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for item in x:
        p.append(pos[item])
        n.append(neg[item])
        nu.append(neu[item])

    trace1 = go.Scatter( x = x, y = p, name = 'Positive', line = dict(color = ('rgb(205,12,24)'),
                        width = 4))
    trace2 = go.Scatter(x = x, y = n, name = 'Negative', line = dict(color = ('rgb(22,96,167)'),
                        width = 4))
    trace3 = go.Scatter(x=x,y = nu, name = 'Neutral', line = dict(color = ('rgb(0,0,0)'),
                        width = 4))
    
    data = [trace1, trace2, trace3]
    layout = dict(title = 'Tweet Sentiment over Time',xaxis = dict(title = 'Month'),yaxis = dict(title = 'Sentiment'),)
    fig = dict(data=data,layout=layout)
    plotly.plot(fig)

