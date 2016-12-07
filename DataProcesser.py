import tDataGatherer
from collections import defaultdict
import matplotlib.pyplot as plt
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

def plotTweetTimesByTime(times):
	timeOfTweets = defaultdict(lambda:0)
	for time in times:
		timeOfTweets[time[2]] += 1
	times = range(24)
	numbers = []
	for time in times:
		numbers.append(timeOfTweets[time])
	fig, ax = plt.subplots()
	width = 1
	rects1 = ax.bar(times,numbers, width)
	ax.set_xticklabels([0, 3, 6, 9, 12, 3, 6, 9])
	ax.set_xticks((0, 3, 6, 9, 12, 15, 18, 21))
	plt.savefig("byTime.png")

<<<<<<< eee6b85c6b395407f740e014f829959dc239be5a

def generateReport (name, handle):
=======
def generateReport (handle):
>>>>>>> git correction, pdf updates
	t = tDataGatherer.TDataGatherer()
	userInfo = t.getUser(handle) #name, bio, profPic
	t.fetchStatuses(handle, 10)
	statuses = t.getFullStatuses()
	tweets = t.getTweets(True, False)
	times = t.getTimes()
	strippedTweets = getStrippedTweets(tweets, True, True, True, True)
<<<<<<< eee6b85c6b395407f740e014f829959dc239be5a
	s = sentimentclassification.SentimentClassifier(strippedTweets)
	#tweetSentiment = s.getTweetSentiment()
	#s.plotTweetResults(tweetsentiment)
	fullText = getFullText(strippedTweets)
	graphWordBag(fullText)
	plotTweetTimesByTime(times)
	pdfW = pdfWriter.pdfWriter(name, handle, "This is a sample bio")
	#pdfW.generatePDF()

generateReport("Mike Rhoades", "@CoachRhoades")
=======
	s = sentimentclassification.SentimentClassifier(tweets)
	tweetSentiment = s.getTweetSentiment()
	#s.plotTweetResults(tweetSentiment)
	topThree = s.plotTopicResults([('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Business & Economy', 'Economic collapse coming'), ('Arts', 'I love museums so much'), ('Arts', 'Museums rock'), ('Sports', 'Go LeBron'), ('Sports', 'Go Lebron!'), ('Home & Domestic Life', 'Momma')])
	fullText = getFullText(strippedTweets)
	graphWordBag(fullText)
	plotTweetTimesByTime(times)
	pdfW = pdfWriter.pdfWriter(userInfo[0], handle, userInfo[1], topThree)
	pdfW.generatePDF()

generateReport("@thebwalk")
>>>>>>> git correction, pdf updates
