import tDataGatherer
from collections import defaultdict
import plotly.plotly as plotly
import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='abhious', api_key='1Tdwg7pmZUvqlMJhNEgD')
plotly.sign_in(username='abhious',api_key='1Tdwg7pmZUvqlMJhNEgD')
import unicodedata
import string
import re
from wordcloud import WordCloud
import PIL
from DatumBox import DatumBox
import pdfWriter
import sentimentclassification
import urllib

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

def getWordBag(strippedTweets, shouldSort):
	wordCounts = defaultdict(lambda: 0)
	for tweet in strippedTweets:
		words = tweet.split()
		for word in words:
			wordCounts[word] += 1
	if shouldSort:
		return sorted(wordCounts.iteritems(), key= lambda (k,v) : v, reverse= True)
	else:
		return wordCounts

def graphWordBag(text):
	wordcloud = WordCloud().generate(text)
	plt.imshow(wordcloud)
	plt.axis("off")
	wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.savefig("wordcloud.png")

def getFullText(tweets):
	fullText = ''
	for tweet in tweets:
		fullText += ' ' + tweet
	return fullText

def plotTweetTimesByDayTime(times):
	timeOfTweets = defaultdict(lambda:0)
	for time in times:
		timeOfTweets[(time[1],time[2])] += 1
	days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	times = range(24)
	dayTimes = []
	numbers = []
	for day in days:
		for time in times:
			dayTimes.append((day,time))
			numbers.append(timeOfTweets[(day,time)])
	fig, ax = plt.subplots()
	width = 1
	rects1 = ax.bar(range(168),numbers, width)
	ax.set_xticklabels(days)
	ax.set_xticks((0, 24, 48, 72, 96, 120, 144))
	plt.show()

def plotTweetTimesByTime(times,user):
        #get tweets per time of the day
        
        tdict = {}
        for time in times:
                if int(time[2]) in tdict:
                        tdict[int(time[2])] += 1
                else:
                        tdict[int(time[2])] = 0
        
        numbers = []
        f = tdict.keys()
        for item in f:
                numbers.append(tdict[item])
        trace1 = go.Scatter( x = f, y = numbers, name = 'Tweets', line = dict(color = ('rgb(205,12,24)'),
                            width = 4))
        data = [trace1]
        layout = dict(title = 'Tweet Rate per Hour for ' + user,xaxis = dict(title = 'Time of Day'),yaxis = dict(title = 'Tweet Count'),)
        fig = dict(data=data,layout=layout)
        plotly.plot(fig)

def generateReport (handle):
	t = tDataGatherer.TDataGatherer()
	userInfo = t.getUser(handle) #name, bio, profPic
	t.fetchStatuses(handle, 10)
	statuses = t.getFullStatuses()
	tweets = t.getTweets(True, False)
	times = t.getTimes()
	strippedTweets = getStrippedTweets(tweets, True, True, True, True)
	s = sentimentclassification.SentimentClassifier(strippedTweets)
	tweetSentiment = s.getTweetSentiment()
	s.plotTweetResults(tweetSentiment)
	s.happinesstimes(strippedTweets,times)
	topThree = s.plotTopicResults([('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Arts', 'Museums rock'), ('Sports', 'Go LeBron'), ('Sports', 'Go Lebron!'), ('Home & Domestic Life', 'Momma')])
	fullText = getFullText(strippedTweets)
	graphWordBag(fullText)
	plotTweetTimesByTime(times)
	pdfW = pdfWriter.pdfWriter(userInfo[0], handle, userInfo[1], topThree)
	pdfW.generatePDF()
	

generateReport("@CoachRhoades")

	


