import numpy as np
import twitter
from DatumBox import DatumBox
import string
import dAccessToken
import tAccessToken
import matplotlib.pyplot as plt
import unicodedata
import re
import plotly.plotly as plotly
import plotly.graph_objs as go
import random
import plotly.tools as tls
tls.set_credentials_file(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')
plotly.sign_in(username='NickJohnsond660', api_key='EceN1JPVhEcH13pY5JlF')

dAccess = dAccessToken.dAccessToken()
datum_box = DatumBox(dAccess.api_key)
import tDataGatherer

t = tDataGatherer.TDataGatherer()
t.fetchStatuses('barackobama', 10)
statuses = t.getFullStatuses()
tweets = t.getTweets()
times = t.getTimes()


def getStrippedTweets(tweets, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags):
    newTweets = []
    for tweet in tweets:
        newTweets.append(stripString(tweet, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags))
    return newTweets


def stripString(s, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
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


def plottweetresults(tweetresults, username):
    # assuming I get the tweetresults in a list
    # pie chart showing percentages of positive,neutral,negative
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

    fig = {
        'data': [{'labels': ['Positive', 'Negative', 'Neutral'],
                  'values': [positive, negative, neutral],
                  'type': 'pie',
                  'marker': {'colors': ['rgb(0, 0, 255)',
                                        'rgb(232, 17, 15)',
                                        'rgb(156, 156, 156)']},
                  'color': '#ffffff'
                  }],
        'layout': {'title': str(username) + ' Positivity Analysis'}
    }

    plotly.plot(fig)


# sizes = [positive,negative,neutral]
# colors = ['blue','red','white']
# explode = (0,0,0)
# labels = 'Positive Tweets','Negative Tweets','Neutral Tweets'
# plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=140)
# plt.axis('equal')
# plt.title(str(username) + 'Tweet Analysis')
# plt.show()

def getTweetTimesByTime(times):
    # get tweets per time of the day
    timeOfTweets = defaultdict(lambda: 0)
    for time in times:
        timeOfTweets[time[2]] += 1
    times = range(24)
    numbers = []
    for time in times:
        numbers.append(timeOfTweets[time])
    return [times, numbers]


def gettweetsentiment(tweets):
    # assuming I get tweets in a list format
    data = []
    for tweet in tweets:
        sentiment = datum_box.twitter_sentiment_analysis(tweet)
        data.append(sentiment)
    return data


def plottopicresults(itemresults):
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

    arts_samp = []
    biz_and_econ_samp = []
    comp_and_tech_samp = []
    health_samp = []
    h_and_d_samp = []
    news_samp = []
    rec_and_act_samp = []
    ref_and_ed_samp = []
    science_samp = []
    shopping_samp = []
    society_samp = []
    sports_samp = []

    for topic, tweet in itemresults:
        if topic == 'Arts':
            arts += 1
            arts_samp.append(tweet)
        elif topic == 'Business & Economy':
            biz_and_econ += 1
            biz_and_econ_samp.append(tweet)
        elif topic == 'Computers & Technology':
            comp_and_tech += 1
            comp_and_tech_samp.append(tweet)
        elif topic == 'Health':
            health += 1
            health_samp.append(tweet)
        elif topic == 'Home & Domestic Life':
            h_and_d += 1
            h_and_d_samp.append(tweet)
        elif topic == 'News':
            news += 1
            news_samp.append(tweet)
        elif topic == 'Recreation & Activities':
            rec_and_act += 1
            rec_and_act_samp.append(tweet)
        elif topic == 'Reference & Education':
            ref_and_ed += 1
            ref_and_ed_samp.append(tweet)
        elif topic == 'Science':
            science += 1
            science_samp.append(tweet)
        elif topic == 'Shopping':
            shopping += 1
            shopping_samp.append(tweet)
        elif topic == 'Society':
            society += 1
            society_samp.append(tweet)
        elif topic == 'Sports':
            sports += 1
            sports_samp.append(tweet)

    # # Makes sure list with tweet has number of tweets in topic too, for easier recognition for choosing random example tweet
    # arts_samp.append(arts)
    # biz_and_econ_samp.append(biz_and_econ)
    # comp_and_tech_samp.append(comp_and_tech)
    # health_samp.append(health)
    # h_and_d_samp.append(h_and_d)
    # news_samp.append(news)
    # rec_and_act_samp.append(rec_and_act)
    # ref_and_ed_samp.append(ref_and_ed)
    # science_samp.append(science)
    # shopping_samp.append(shopping)
    # society_samp.append(society)
    # sports_samp.append(sports)

    # Gets top three topics to shade them differently

    tweets_by_topic = [arts, biz_and_econ, comp_and_tech, health, h_and_d, news,
                       rec_and_act, ref_and_ed, science, shopping, society, sports]

    tweets_by_topic = sorted(tweets_by_topic)

    most_used_topic = tweets_by_topic.pop()
    second_used_topic = tweets_by_topic.pop()
    third_used_topic = tweets_by_topic.pop()

    top_three = [most_used_topic, second_used_topic, third_used_topic]
    print most_used_topic
    print second_used_topic
    print third_used_topic

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
    plotly.plot(fig, filename='color-bar')

    sample
    arts_samp = []
    biz_and_econ_samp = []
    comp_and_tech_samp = []
    health_samp = []
    h_and_d_samp = []
    news_samp = []
    rec_and_act_samp = []
    ref_and_ed_samp = []
    science_samp = []
    shopping_samp = []
    society_samp = []
    sports_samp = []

    #sample_tweets = [sample_from_top_topic, sample_from_sec_topic, sample_from_third_topic]
    #print sample_tweets





def getsenttweet(tweets):
    """gives you a list of lists where first element is the topic and second is the tweet for every tweet"""
    data = []
    for tweet in tweets:
        topic = datum_box.topic_classification(tweet)
        data.append([topic, tweet])
    return data


plottopicresults([('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'),
                  ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'),
                  ('Arts', 'I love museums so much'), ('Arts', 'Museums rock'), ('Sports', 'Go LeBron'), ('Sports', 'Go Lebron!'), ('Home & Domestic Life', 'Momma')])


# strippedtweets = getStrippedTweets(tweets, True, True, True, True)
# tweetsentiment = gettweetsentiment(strippedtweets)
# plottweetresults(tweetsentiment, 'barackobama')