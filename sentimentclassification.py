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
import plotly.plotly as plotly
import plotly.graph_objs as go
import plotly.tools as tls
from collections import defaultdict

<<<<<<< eee6b85c6b395407f740e014f829959dc239be5a
=======

>>>>>>> git correction, pdf updates
class SentimentClassifier:
    def __init__ (self, tweets):
        dAccess = dAccessToken.dAccessToken()
        self.datumBox = DatumBox(dAccess.api_key)
        self.tweets = tweets
        tls.set_credentials_file(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
        plotly.sign_in(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')

    def plotTweetResults(self, tweetResults):
        #assuming I get the tweetresults in a list 
        #pie chart showing percentages of positive,neutral,negative
        positive = 0
        negative = 0
        neutral = 0
        for item in tweetResults:
            if item == 'positive':
                positive += 1
            elif item == 'negative':
                negative += 1
            else:
                neutral += 1
        fig = {
            'data': [{'labels': ['Positive', 'Negative', 'Neutral'],
                      'values': [positive, negative, neutral],
                      'type': 'pie',
                      'marker': {'colors': ['rgb(0, 0, 255)',
                                            'rgb(232, 17, 15)',
                                            'rgb(156, 156, 156)']},
                      }],
            'layout': {'title': ' Positivity Analysis'}
        }
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


    def getTweetSentiment(self):
        #assuming I get tweets in a list format
        data = []
        for tweet in self.tweets:
            # print tweet
            ##sentiment = self.datumBox.twitter_sentiment_analysis(tweet)
            sentiment = random.choice(["positive", "negative", "neutral"])
            data.append(sentiment)
        return data

    def plotTopicResults(self, itemresults):
        # assuming I get the itemresults in a tuple
        # bar chart showing top topics
        global topic_counts, topics, colors_by_topic
        arts = 0
        biz_and_econ = 0
        comp_and_tech = 0
        health = 0
        h_and_d = 0
        news = 0
        rec_and_act = 0
        ref_and_ed = 0
        science = 0
        shopping = 0
        society = 0
        sports = 0

        topicDict = defaultdict(lambda : [])
        for topic, tweet in itemresults:
            topicDict[topic].append(tweet)

        for topic, tweet in itemresults:
            if topic == 'Arts':
                arts += 1
            elif topic == 'Business & Economy':
                biz_and_econ += 1
            elif topic == 'Computers & Technology':
                comp_and_tech += 1
            elif topic == 'Health':
                health += 1
            elif topic == 'Home & Domestic Life':
                h_and_d += 1
            elif topic == 'News':
                news += 1
            elif topic == 'Recreation & Activities':
                rec_and_act += 1
            elif topic == 'Reference & Education':
                ref_and_ed += 1
            elif topic == 'Science':
                science += 1
            elif topic == 'Shopping':
                shopping += 1
            elif topic == 'Society':
                society += 1
            elif topic == 'Sports':
                sports += 1

        # Gets top three topics to shade them differently

        tweets_by_topic = [arts, biz_and_econ, comp_and_tech, health, h_and_d, news,
                           rec_and_act, ref_and_ed, science, shopping, society, sports]

        tweets_by_topic = sorted(tweets_by_topic)

        most_used_topic = tweets_by_topic.pop()
        second_used_topic = tweets_by_topic.pop()
        third_used_topic = tweets_by_topic.pop()

        tweets_by_topic = [arts, biz_and_econ, comp_and_tech, health, h_and_d, news,
                           rec_and_act, ref_and_ed, science, shopping, society, sports]


        # Colors topics based on their use
        colors_by_topic = []
        for topic in tweets_by_topic:
            if topic == most_used_topic:
                colors_by_topic.append('rgba(232, 17, 15, 1)')
            elif topic == second_used_topic:
                colors_by_topic.append('rgba(238, 87, 85, 0.8)')
            elif topic == third_used_topic:
                colors_by_topic.append('rgba(231, 157, 155, 0.8)')
            else:
                colors_by_topic.append('rgba(204, 204, 204, 0.5')

        topics = ['Arts', 'Business & Economy', 'Computers & Technology',
                  'Health', 'Home & Domestic Life', 'News', 'Recreation & Activities',
                  'Reference & Education', 'Science', 'Shopping', 'Society', 'Sports']
        topic_counts = [arts, biz_and_econ, comp_and_tech, health, h_and_d, news,
                        rec_and_act, ref_and_ed, science, shopping, society, sports]
        trace0 = go.Bar(
                x=topics, y=topic_counts,
                marker=dict(
                    color=colors_by_topic),
            )

        data = [trace0]
        layout = go.Layout(
                title='Top Three Tweet Topics for' + 'Test',
                xaxis=dict(tickangle=-45),
                margin=go.Margin(b=135)
            )

        fig = go.Figure(data=data, layout=layout)
        #plotly.plot(fig, filename='color-bar')

        top_topic = max(topicDict, key=lambda x: len(topicDict[x]))
        top_topic_tweet = random.choice(topicDict[top_topic])
        del topicDict[top_topic]

        second_topic = max(topicDict, key=lambda x: len(topicDict[x]))
        second_topic_tweet = random.choice(topicDict[second_topic])
        del topicDict[second_topic]

        third_topic = max(topicDict, key=lambda x: len(topicDict[x]))
        third_topic_tweet = random.choice(topicDict[third_topic])
        del topicDict[third_topic]

        return [(str(top_topic), str(top_topic_tweet)),
                (str(second_topic), str(second_topic_tweet)),
                (str(third_topic), str(third_topic_tweet))]

    def getSentTweet(tweets):
        """gives you a list of lists where first element is the topic and second is the tweet for every tweet"""
        data = []
        for tweet in tweets:
            topic = datum_box.topic_classification(tweet)
            data.append([topic, tweet])
        return data

<<<<<<< eee6b85c6b395407f740e014f829959dc239be5a
    def plottweetresults(self, tweetresults,username):
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


    def getTweetSentiment(self):
        #assuming I get tweets in a list format
        data = []
        for tweet in self.tweets:
            # print tweet
            sentiment = self.datumBox.twitter_sentiment_analysis(tweet)
            data.append(sentiment)
        return data

    def getsenttweet(self, tweets):
        #gives you a list of lists where first element is the topic and the second is the tweet for every tweet
        #should not be in the class, should be in different class
        data = []
        for tweet in tweets:
            topic = datum_box.topic_classification(tweet)
            data.append([topic,tweet])
        return data

    def happinesstimes(self, tweets,times):
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
=======
>>>>>>> git correction, pdf updates

#plotTopicResults([('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'),
#    ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'),
#                      ('Arts', 'I love museums so much'), ('Arts', 'Museums rock'), ('Sports', 'Go LeBron'), ('Sports', 'Go Lebron!'), ('Home & Domestic Life', 'Momma')])