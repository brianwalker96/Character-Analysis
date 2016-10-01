import twitter
import tAccessToken #STORE AS LOCAL COPY - NOT ON GITHUB. NEVER COMMIT THIS

keyData = tAccessToken.AccessToken()
api = twitter.Api(consumer_key= keyData.consumer_key,
                  consumer_secret= keyData.consumer_secret,
                  access_token_key= keyData.access_token_key,
                  access_token_secret= keyData.access_token_secret)
#NOTE ONLY 100 API CALLS PER HOUR
users = api.GetFriends()
print users