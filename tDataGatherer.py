import twitter
import tAccessToken #STORE AS LOCAL COPY - NOT ON GITHUB. NEVER COMMIT THIS
import string
import urllib

class TDataGatherer:
	def __init__(self):
		#Store the key and api
		print "TDataGatherer - initializing"
		self.key = tAccessToken.AccessToken()
		self.api = twitter.Api(consumer_key= self.key.consumer_key,
        	          consumer_secret= self.key.consumer_secret,
            	      access_token_key= self.key.access_token_key,
                	  access_token_secret= self.key.access_token_secret)

		#NOTE ONLY 100 API CALLS PER HOUR

	def getUser(self, username, utc):
		self.user = self.api.GetUser(screen_name = username)
		if (utc == 0) :
			self.offset = self.user.utc_offset / 3600
		else :
			self.offset = utc
		print "TDataGatherer - offset = " + str(self.offset)
		print "TDataGatherer - user info fetched"
		print self.user.profile_image_url
		urllib.urlretrieve(self.user.profile_image_url.replace("_normal.jpg", ".jpg").replace("_normal.jpeg", ".jpeg"), "prof_pic.jpg")
		print "TDataGatherer - profile picture stored"
		return [self.user.name, self.user.description]


	def fetchStatuses(self, username, maxCount): #maxCount max is 3200
		#Just get statuses here, don't process at all
		print "TDataGatherer - fetching " + str(maxCount) + " tweets from " + str(username)
		batchCount = min(200, maxCount) #200 fetch limit at a time
		print "TDataGatherer - fetching " + str(batchCount) + " of " + str(maxCount)
		self.statuses = self.api.GetUserTimeline(screen_name = username, count = batchCount)
		fetchCount = batchCount
		while (fetchCount < maxCount) :
			lastTweet = self.statuses[-1].id
			print "TDataGatherer - fetching " + str(fetchCount) + " of " + str(maxCount)
			newStatuses = self.api.GetUserTimeline(screen_name = username, count = min(maxCount-fetchCount, batchCount), max_id = lastTweet)
			self.statuses = self.statuses + newStatuses[1:]
			fetchCount += batchCount

	def getFullStatuses(self):
		#don't process just return the statuses
		return self.statuses

	def getTweets(self, userTweets, retweets):
		#only the tweets themselves
		tweets = []
		printable = set(string.printable)
		for status in self.statuses:
			if ((userTweets and not status.retweeted_status) or (retweets and status.retweeted_status)):
				print status.retweeted_status
				tweets.append(status.text)#Unicode / ascii errors when looking at strings
		return tweets

	def getTimes(self, userTweets, retweets):
		print "TDataGatherer - formatting time"
		timeOfTweets = []
		previousDay = {"Sun":"Sat", "Mon":"Sun", "Tue":"Mon", "Wed":"Tue", "Thu":"Wed", "Fri":"Thu", "Sat":"Fri"}
		nextDay = {"Sun":"Mon", "Mon":"Tue", "Tue":"Wed", "Wed":"Thu", "Thu":"Fri", "Fri":"Sat", "Sat":"Sun"}
		for status in self.statuses:
			if ((userTweets and not status.retweeted_status) or (retweets and status.retweeted_status)):
				year = int(status.created_at[26:30])
				month = status.created_at[4:7]
				day = status.created_at[0:3]
				hour = int(status.created_at[11:13]) + self.offset
				if hour < 0:
			 		hour += 24
			 		day = previousDay[day]
				if hour > 24:
			 		hour -= 24
			 		day = nextDay[day]		
				timeOfTweets.append((year,day, hour, month))
		return timeOfTweets
