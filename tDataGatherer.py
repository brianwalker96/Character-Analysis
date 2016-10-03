import twitter
import tAccessToken #STORE AS LOCAL COPY - NOT ON GITHUB. NEVER COMMIT THIS

class TDataGatherer:
	def __init__(self):
		#Store the key and api
		self.key = tAccessToken.AccessToken()
		self.api = twitter.Api(consumer_key= self.key.consumer_key,
        	          consumer_secret= self.key.consumer_secret,
            	      access_token_key= self.key.access_token_key,
                	  access_token_secret= self.key.access_token_secret)
		#NOTE ONLY 100 API CALLS PER HOUR

	def fetchStatuses(self, username, maxCount): #maxCount max is 3200
		#Just get statuses here, don't process at all
		batchCount = min(200, maxCount) #200 fetch limit
		self.statuses = self.api.GetUserTimeline(screen_name = username, count = batchCount)
		fetchCount = batchCount
		while (fetchCount < maxCount) :
			lastTweet = self.statuses[-1].id
			newStatuses = self.api.GetUserTimeline(screen_name = username, count = min(maxCount-fetchCount, batchCount), max_id = lastTweet)
			self.statuses = self.statuses + newStatuses 
			fetchCount += batchCount

	def getFullStatuses(self):
		#don't process just return the statuses
		return self.statuses

	def getTweets(self):
		#only the tweets themselves
		tweets = []
		for status in self.statuses:
			tweets.append(str(status.text))
		return tweets

	def getTimes(self):
		#only the times themselves
		timeOfTweets = []
		for status in self.statuses:
			year = int(status.created_at[26:30])
			day = status.created_at[0:3]
			hour = int(status.created_at[11:13])
			timeOfTweets.append((year,day, hour))
		return timeOfTweets
