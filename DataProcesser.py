import tDataGatherer
from collections import defaultdict
import matplotlib.pyplot as plt

t = tDataGatherer.TDataGatherer()
t.fetchStatuses('bencgauld', 1000)
statuses = t.getFullStatuses()
tweets = t.getTweets()
times = t.getTimes()

#takes the texts of fetched tweets and a boolean of whether to sort the return
#returns either sorted list or default dict with the counts of each word
def getWordCount(tweets, shouldSort):
	wordCounts = defaultdict(lambda: 0)
	for tweet in tweets:
		words = tweet.split()
		for word in words:
			wordCounts[word] += 1
	if shouldSort:
		return sorted(wordCounts.iteritems(), key= lambda (k,v) : v, reverse= True)
	else:
		return wordCounts

#print getWordCount(tweets, True)

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

#plotTweetTimesByDayTime(times)

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
	plt.show()

#plotTweetTimesByTime(times)