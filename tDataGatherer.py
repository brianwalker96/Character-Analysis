import twitter
import tAccessToken #STORE AS LOCAL COPY - NOT ON GITHUB. NEVER COMMIT THIS
from collections import defaultdict

keyData = tAccessToken.AccessToken()
api = twitter.Api(consumer_key= keyData.consumer_key,
                  consumer_secret= keyData.consumer_secret,
                  access_token_key= keyData.access_token_key,
                  access_token_secret= keyData.access_token_secret)
#NOTE ONLY 100 API CALLS PER HOUR

# users = api.GetFriends()
# for user in users:
# 	print 'Name: ' + str(user.screen_name)
# 	print 'Following: ' + str(user.friends_count)
# 	print 'Followers: ' + str(user.followers_count)
# 	print 

statuses = api.GetUserTimeline(screen_name = 'bencgauld')
timeOfTweets = defaultdict(lambda:defaultdict(lambda:0))
timesList = []
#combinedStatus = ''
for status in statuses:
	timesList.append(status.created_at)
	print status.created_at
	year = status.created_at[26:30]
	day = status.created_at[0:3]
	hour = status.created_at[11:13]
	#combinedStatus += ' ' + status.text   UNICODE ENCODING ERROR
	timeOfTweets[year][(day,hour)] += 1

print timeOfTweets
#print combinedStatus