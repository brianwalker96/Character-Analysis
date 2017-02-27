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
    def __init__ (self, rawTweets, tweets, times):
        print "SentimentClassifier - initializing"
        dAccess = dAccessToken.dAccessToken()
        self.datumBox = DatumBox(dAccess.api_key)
        self.tweets = tweets
        self.rawTweets = rawTweets
        self.times = times
        self.colorMapping = {"positive": 'rgb(100, 100, 255)', "negative": 'rgb(232, 17, 15)', "neutral": 'rgb(156, 156, 156)'}
        #tls.set_credentials_file(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
        #plotly.sign_in(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
        #Alternate Credentials
        tls.set_credentials_file(username='abhious', api_key='1Tdwg7pmZUvqlMJhNEgD')
        plotly.sign_in(username='abhious',api_key='1Tdwg7pmZUvqlMJhNEgD')

    def getTweetSentiment(self, testing, shouldPlot):
        print "SentimentClassifier - determining sentiment"
        self.sentiments = []
        i = 0
        for tweet in self.tweets:
            sentiment = ""
            if i % 2 == 0:
                if testing:
                    sentiment = random.choice(["positive", "negative", "neutral"])
                else :
                    sentiment = self.datumBox.twitter_sentiment_analysis(tweet)
                self.sentiments.append(sentiment)
                print (tweet + " - " + sentiment)
                if len(self.sentiments) % 25 == 0:
                    print "SentimentClasiiffier - determining sentiment " + str(len(self.sentiments))
            i += 1
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
            labels.append(sent.title())
            values.append(numOfSent[sent])
            colors.append(self.colorMapping[sent])
        fig = {
            'data': [{'labels': labels,
                      'values': values,
                      'type': 'pie',
                      'marker': {'colors': colors},
                      }],
            'layout': {'title': '<b>Sentiment Distribution</b>'}
        }
        plotly.image.save_as(fig, filename='sentiment_pie_chart.png')           
    
    def getTweetTopics(self, testing, shouldPlot):
        print "SentimentClassifier - determining tweets' topic"
        self.topics = []
        i = 0
        for tweet in self.tweets:
            if i % 5 == 0:
                topic = ""
                if testing:
                    topic = random.choice(["Arts", 'Business & Economy', 'Sports', 'Home & Domestic Life'])
                else : 
                    topic = self.datumBox.topic_classification(tweet)
                self.topics.append(topic)
                if len(self.sentiments) % 25 == 0:
                    print "SentimentClasiiffier - determining topic " + str(len(self.sentiments)) 
            i += 1
        if shouldPlot:
            return self.plotTopicResults() 

    def sentimentOverTime(self):
        print 'SentimentClassifier - sentiment over time graph'
        sampleTimes = []
        for i in range(len(self.times)):
            if i % 5 == 0:
                sampleTimes.append(self.times[i])
        #Make monthly (w/ year) counts by sentiment
        sentTimes = zip(self.sentiments, sampleTimes)
        monthCts = defaultdict(lambda: defaultdict(lambda: 0))
        for sent,time in sentTimes:
            monthCts[time[3] + " " + str(time[0])][sent] += 1
        
        #create list of contiguous months by starting at oldest month, increasing to newest month
        curMonth = self.times[-1][3]
        curYear = self.times[-1][0]
        newestMonth = self.times[0][3] 
        newestYear = self.times[0][0]
        nextMonth  = {"Jan" : "Feb", "Feb" : "Mar", "Mar" : "Apr", "Apr" : "May", "May" : "Jun", "Jun" : "Jul", "Jul" : "Aug", "Aug" : "Sep", "Sep" : "Oct", "Oct" : "Nov", "Nov" : "Dec", "Dec" : "Jan" }
        months = []
        while (curMonth != newestMonth or curYear != newestYear):
            months.append(curMonth + " " + str(curYear))
            curMonth = nextMonth[curMonth]
            if (curMonth == "Jan"):
                curYear += 1

        #make the data points by combining the list of contiguous months and monthly counts
        pos = []
        neg = []
        neu = []
        for month in months:
            monthTweets = (monthCts[month]["positive"] + monthCts[month]["negative"] + monthCts[month]["neutral"]) * 1.0
            if monthTweets > 0 :
                pos.append(monthCts[month]["positive"] / monthTweets)
                neg.append(monthCts[month]["negative"] / monthTweets)
                neu.append(monthCts[month]["neutral"] / monthTweets)
            else :
                pos.append(0)
                neg.append(0)
                neu.append(0)

        #Graph
        posTrace = go.Scatter( x = months, y = pos, name = 'Positive', line = dict(color = ('rgb(205,12,24)'),
                            width = 4))
        negTrace = go.Scatter(x = months, y = neg, name = 'Negative', line = dict(color = ('rgb(22,96,167)'),
                            width = 4))
        neuTrace = go.Scatter(x=months ,y = neu, name = 'Neutral', line = dict(color = ('rgb(0,0,0)'),
                            width = 4))
        sentData = [posTrace, negTrace, neuTrace]
        layout = dict(title = '<b>Tweet Sentiment over Time</b>',xaxis = dict(title = 'Month'),yaxis = dict(title = 'Percentage of Tweets'),)
        fig = dict(data=sentData,layout=layout)
        plotly.image.save_as(fig, filename='sentiment_over_time.png')

    def plotTopicResults(self):
        print "SentimentClassifier - topic bar graph"
        # bar chart showing top topics
        sampleTweets = []
        for i in range(len(self.times)):
            if i % 5 == 0:
                sampleTweets.append(self.tweets[i])

        topicTweet = zip(self.topics, sampleTweets)

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
        for i in range(len(topicTweet)):
            topicDict[topicTweet[i][0]].append(i)

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
        numTweets = (arts + biz_and_econ + comp_and_tech + health + h_and_d + news + rec_and_act + ref_and_ed + science + shopping + society + sports) * 1.0
        topic_counts = [arts / numTweets, biz_and_econ / numTweets, comp_and_tech / numTweets, health / numTweets, h_and_d / numTweets, news / numTweets,
                        rec_and_act / numTweets, ref_and_ed / numTweets, science / numTweets, shopping /numTweets, society / numTweets , sports /numTweets]
        trace0 = go.Bar(
                x=topics, y=topic_counts,
                marker=dict(
                    color=colors_by_topic),
            )

        data = [trace0]
        layout = go.Layout(
                title='<b>Topic Distribution</b>',
                xaxis=dict(tickangle=-45),
                yaxis = dict(title = 'Percentage of Tweets'),
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

        return [(str(top_topic), self.rawTweets[top_topic_tweet]),
                (str(second_topic), self.rawTweets[second_topic_tweet]),
                (str(third_topic), self.rawTweets[third_topic_tweet])]

    def findAdultContent(self):
        badWords = ["anal", "anus", " ass ", "asshole" , "bastard", "bitch", "biatch", "blood", "blow ", "boner", "boob", " bum", "butt ", "butts", "clit", "cock",
        "crap", "cunt", "damn", "dick", "dildo", "dyke", "fag", "fuck", " hell ", " homo", "gay", "jerk", "jizz", "nigg", "penis", "piss", "poop", "prick",
        "pube", "pussy", "queer", "sack", "sex", "shit", "slut", " tit ", " tits ", "vagina", "wank", "whore", "weed", "marijuana", "cocaine", " pot ", "pothead", "mary jane",
        "acid", "crack", "lsd", "dank", "copulate", "cum", "suck", "69", "fingering", "fisting", "broccoli"]
        flagged = []
        idxs = []
        for i in range(len(self.tweets)):
            for badWord in badWords:
                if badWord in self.tweets[i]:
                    print badWord + ' IS IN ' + self.tweets[i]
                    idxs.append(i)
                    break
        for idx in idxs:
            flagged.append(self.rawTweets[idx])
        return flagged
    


    

