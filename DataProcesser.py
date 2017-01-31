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

def getMonthDifference(month1, month2):
	monthOrder = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
	return monthOrder[month2] - monthOrder[month1]

def plotTweetTimesByTime(times):
	print 'plotTweetTimesByTime - time bar chart'
	totalHours = (((times[0][0] - times[-1][0]) * 365 + getMonthDifference(times[0][3], times[-1][3])) * 30) * 24.0
	timeDict = defaultdict(lambda: 0)
	for time in times:
	    timeDict[int(time[2])] += 1
	tweetsPerHour = []   
	for time in range(24):
	    tweetsPerHour.append(timeDict[time]/totalHours)

	trace0 = go.Bar(
                x=['12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM',
                '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM'],
                y=tweetsPerHour,
                marker=dict(
                    color=('rgb(205,12,24)')
            ))
	data = [trace0]
	layout = go.Layout(
	            title='<b>Time Distribution</b>',
	            xaxis=dict(tickangle=-45),
	            yaxis = dict(title = 'Tweets Per Hour'),
	            margin=go.Margin(b=135)
	)

	fig = go.Figure(data=data, layout=layout)
	plotly.image.save_as(fig, filename='tweets_by_time.png')

def generateReport (handle, testing):
	t = tDataGatherer.TDataGatherer()
	userInfo = t.getUser(handle) #(name, bio)
	t.fetchStatuses(handle, 1500)
	statuses = t.getFullStatuses()
	tweets = t.getTweets(True, False)
	times = t.getTimes()
	strippedTweets = stripStrings(tweets, True, True, True, True)
	fullText = concatStrings(strippedTweets)
	wc = wordCloud.WordCloudHelper()
	wc.graphWords(fullText)
	s = sentimentclassification.SentimentClassifier(tweets, strippedTweets, times)
	s.getTweetSentiment(testing, True)
	s.sentimentOverTime()
	topicTweets = s.getTweetTopics(testing, True)
	plotTweetTimesByTime(times)
	flaggedTweets = s.findAdultContent()
	pdfW = pdfWriter.PDFWriter(userInfo[0], handle, userInfo[1], topicTweets, flaggedTweets)
	pdfW.generatePDF()
	

generateReport("@RealDonaldTrump", False)
	


