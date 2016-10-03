import tDataGatherer
from collections import defaultdict
import matplotlib.pyplot as plt

t = tDataGatherer.TDataGatherer()
t.fetchStatuses('bencgauld', 1000)
statuses = t.getFullStatuses()
tweets = t.getTweets()
times = t.getTimes()

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
	plt.show()


plotTweetTimesByDayTime(times)
plotTweetTimesByTime(times)