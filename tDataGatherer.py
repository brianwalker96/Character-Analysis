import twitter
import tAccessToken #STORE AS LOCAL COPY - NOT ON GITHUB. NEVER COMMIT THIS
import string
import urllib

class TDataGatherer:
	def __init__(self):
		#Store the key and api
		self.key = tAccessToken.AccessToken()
		self.api = twitter.Api(consumer_key= self.key.consumer_key,
        	          consumer_secret= self.key.consumer_secret,
            	      access_token_key= self.key.access_token_key,
                	  access_token_secret= self.key.access_token_secret)
		#NOTE ONLY 100 API CALLS PER HOUR

	def getUser(self, username):
		self.user = self.api.GetUser(screen_name = username)
		urllib.urlretrieve(self.user.profile_image_url.replace("_normal.jpg", ".jpg"), "prof-pic.jpg")
		return [self.user.name, self.user.description]

	def fetchStatuses(self, username, maxCount): #maxCount max is 3200
		#Just get statuses here, don't process at all
		batchCount = min(200, maxCount) #200 fetch limit
		self.statuses = self.api.GetUserTimeline(screen_name = username, count = batchCount)
		fetchCount = batchCount
		while (fetchCount < maxCount) :
			lastTweet = self.statuses[-1].id
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
			if ((userTweets and not status.retweeted) or (retweets and status.retweeted)):
				tweets.append(status.text)#Unicode / ascii errors when looking at strings
		return tweets

	def getTimes(self):
		#only the times themselves
		#issue-- accounting for timezone - user is supposed to have utc offset but doesn't...
		timeOfTweets = []
		previousDay = {"Sun":"Sat", "Mon":"Sun", "Tue":"Mon", "Wed":"Tue", "Thu":"Wed", "Fri":"Thu", "Sat":"Fri"}
		nextDay = {"Sun":"Mon", "Mon":"Tue", "Tue":"Wed", "Wed":"Thu", "Thu":"Fri", "Fri":"Sat", "Sat":"Sun"}
		for status in self.statuses:
			year = int(status.created_at[26:30])
			month = status.created_at[4:7]
			day = status.created_at[0:3]
			hour = int(status.created_at[11:13])
			timeOfTweets.append((year,day, hour, month))
		return timeOfTweets
