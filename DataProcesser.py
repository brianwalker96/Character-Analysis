import tDataGatherer
import unicodedata
import string
import re
import wordCloud
import sentimentclassification
import plotly.plotly as plotly
import plotly.graph_objs as go
import pdfWriter
from collections import defaultdict
#import plotly.tools as tls
#import PIL
#import urllib

def stripStrings(strings, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags):
	newStrings = []
	print "stripStrings - stripping " + str(len(strings)) + " strings"
	for string in strings:
		newStrings.append(stripString(string, shouldStripPunct, shouldStripURLs, shouldStripUsers, shouldStripHashTags))
	return newStrings

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

def concatStrings(strings):
	print "concatStrings - concatenating " + str(len(strings)) + " strings"
	fullText = ''
	for string in strings:
		fullText += ' ' + string
	return fullText

# def getWordBag(strippedTweets, shouldSort):
# 	wordCounts = defaultdict(lambda: 0)
# 	for tweet in strippedTweets:
# 		words = tweet.split()
# 		for word in words:
# 			wordCounts[word] += 1
# 	if shouldSort:
# 		return sorted(wordCounts.iteritems(), key= lambda (k,v) : v, reverse= True)
# 	else:
# 		return wordCounts

# def plotTweetTimesByDayTime(times):
# 	timeOfTweets = defaultdict(lambda:0)
# 	for time in times:
# 		timeOfTweets[(time[1],time[2])] += 1
# 	days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# 	times = range(24)
# 	dayTimes = []
# 	numbers = []
# 	for day in days:
# 		for time in times:
# 			dayTimes.append((day,time))
# 			numbers.append(timeOfTweets[(day,time)])
# 	fig, ax = plt.subplots()
# 	width = 1
# 	rects1 = ax.bar(range(168),numbers, width)
# 	ax.set_xticklabels(days)
# 	ax.set_xticks((0, 24, 48, 72, 96, 120, 144))
# 	plt.show()

def plotTweetTimesByTime(times):
	print 'plotTweetTimesByTime - time bar chart'
	timeDict = defaultdict(lambda: 0)
	for time in times:
	    timeDict[int(time[2])] += 1
	tweetsPerHour = []   
	for time in range(24):
	    tweetsPerHour.append(timeDict[time])
	trace1 = go.Scatter( x = range(24), y = tweetsPerHour, name = 'Tweets', line = dict(color = ('rgb(205,12,24)'),
	                    width = 4))
	data = [trace1]
	layout = dict(title = 'Tweet Count per Time Of Day' ,xaxis = dict(title = 'Time of Day'),yaxis = dict(title = 'Tweet Count'),)
	fig = dict(data=data,layout=layout)
	plotly.image.save_as(fig, filename='tweets_by_time.png')

def generateReport (handle, testing):
	t = tDataGatherer.TDataGatherer()
	userInfo = t.getUser(handle) #(name, bio)
	t.fetchStatuses(handle, 200)
	statuses = t.getFullStatuses()
	tweets = t.getTweets(True, False)
	times = t.getTimes()
	strippedTweets = stripStrings(tweets, True, True, True, True)
	fullText = concatStrings(strippedTweets)
	wc = wordCloud.WordCloudHelper()
	wc.graphWords(fullText)
	s = sentimentclassification.SentimentClassifier(strippedTweets, times)
	s.getTweetSentiment(testing, True)
	s.sentimentOverTime()
	topicTweets = s.getTweetTopics(testing, True)
	plotTweetTimesByTime(times)
	pdfW = pdfWriter.PDFWriter(userInfo[0], handle, userInfo[1], topicTweets)
	pdfW.generatePDF()
	

generateReport("@CoachRhoades", True)

	


