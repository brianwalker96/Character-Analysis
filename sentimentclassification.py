import twitter
from DatumBox import DatumBox
import string
import dAccessToken
import tAccessToken
import re
from plotly import plotly
import plotly.plotly as plotly
import plotly.tools as tls
import tDataGatherer
import plotly.graph_objs as go
import random
import plotly.plotly as plotly
import plotly.graph_objs as go
import plotly.tools as tls
from collections import defaultdict

class SentimentClassifier:
    def __init__ (self, tweets, times):
        print "SentimentClassifier - initializing"
        dAccess = dAccessToken.dAccessToken()
        self.datumBox = DatumBox(dAccess.api_key)
        self.tweets = tweets
        self.times = times
        self.colorMapping = {"positive": 'rgb(0, 0, 255)', "negative": 'rgb(232, 17, 15)', "neutral": 'rgb(156, 156, 156)'}
        #tls.set_credentials_file(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
        #plotly.sign_in(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
        #Alternate Credentials
        tls.set_credentials_file(username='abhious', api_key='1Tdwg7pmZUvqlMJhNEgD')
        plotly.sign_in(username='abhious',api_key='1Tdwg7pmZUvqlMJhNEgD')

    def getTweetSentiment(self, testing, shouldPlot):
        print "SentimentClassifier - determining sentiment"
        self.sentiments = []
        for tweet in self.tweets:
            if len(self.sentiments) % 25 == 0:
                print "SentimentClasiiffier - determining sentiment " + str(len(self.sentiments))
            sentiment = ""
            if testing:
                sentiment = random.choice(["positive", "negative", "neutral"])
            else :
                sentiment = self.datumBox.twitter_sentiment_analysis(tweet)
            self.sentiments.append(sentiment)
        if shouldPlot:
            self.plotSentimentPie()

    def plotSentimentPie(self):
        print "SentimentClassifier - sentiment pie chart"
        numOfSent = defaultdict(lambda: 0)
        labels = []
        values = []
        colors = []
        for sent in self.sentiments:
            numOfSent[sent] += 1
        for sent in numOfSent:
            labels.append(sent)
            values.append(numOfSent[sent])
            colors.append(self.colorMapping[sent])
        fig = {
            'data': [{'labels': labels,
                      'values': values,
                      'type': 'pie',
                      'marker': {'colors': colors},
                      }],
            'layout': {'title': ' Positivity Analysis'}
        }
        plotly.image.save_as(fig, filename='sentiment_pie_chart.png')           
    
    def getTweetTopics(self, testing, shouldPlot):
        print "SentimentClassifier - determining tweets' topic"
        self.topics = []
        for tweet in self.tweets:
            topic = ""
            if testing:
                topic = random.choice(["Arts", 'Business & Economy', 'Sports', 'Home & Domestic Life'])
            else : 
                topic = datum_box.topic_classification(tweet)
            self.topics.append(topic) 
        if shouldPlot:
            return self.plotTopicResults() 

    def sentimentOverTime(self):
        #BUG - edge case - going over multiple years of time
        print 'SentimentClassifier - sentiment over time graph'
        sentTimes = zip(self.sentiments, self.times)
        monthCts = defaultdict(lambda: defaultdict(lambda: 0))
        for sent,time in sentTimes:
            monthCts[time[3]][sent] += 1
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        pos = {}
        neg = {}
        neu = {}
        for month in months:
            pos[month] = monthCts[month]['positive']
            neg[month] = monthCts[month]['negative']
            neu[month] = monthCts[month]['neutral']
        p = []
        n = []
        nu = []
        for item in months:
            p.append(pos[item])
            n.append(neg[item])
            nu.append(neu[item])

        trace1 = go.Scatter( x = months, y = p, name = 'Positive', line = dict(color = ('rgb(205,12,24)'),
                            width = 4))
        trace2 = go.Scatter(x = months, y = n, name = 'Negative', line = dict(color = ('rgb(22,96,167)'),
                            width = 4))
        trace3 = go.Scatter(x=months ,y = nu, name = 'Neutral', line = dict(color = ('rgb(0,0,0)'),
                            width = 4))
        
        data = [trace1, trace2, trace3]
        layout = dict(title = 'Tweet Sentiment over Time',xaxis = dict(title = 'Month'),yaxis = dict(title = 'Sentiment'),)
        fig = dict(data=data,layout=layout)
        plotly.image.save_as(fig, filename='sentiment_over_time.png')

    def plotTopicResults(self):
        print "SentimentClassifier - topic bar graph"
        # bar chart showing top topics
        topicTweet = zip(self.topics, self.tweets)

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
        for topic, tweet in topicTweet:
            topicDict[topic].append(tweet)

        for topic, tweet in topicTweet:
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
        plotly.image.save_as(fig, filename='topic_bar.png')

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

    


    

