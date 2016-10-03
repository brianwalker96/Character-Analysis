import tDataGatherer
from collections import defaultdict

t = tDataGatherer.TDataGatherer()
t.fetchStatuses('bencgauld', 3200)
statuses = t.getFullStatuses()
tweets = t.getTweets()
print tweets
times = t.getTimes()

def printTweetTimesByDayTime(times):
	timeOfTweets = defaultdict(lambda:0)
	for time in times:
		timeOfTweets[(time[1],time[2])] += 1
	days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	times = range(24)
	for time in times:
		for day in days:
			print str(day) + " " + str(time) + " :" + str(timeOfTweets[(day,time)]),
		print

printTweetTimesByDayTime(times)
