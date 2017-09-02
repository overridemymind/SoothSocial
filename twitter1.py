import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('')
print(dir(public_tweets))

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity <= 0:
		print(20*'-')
		print(tweet.text)
		print('\n' + str(analysis.sentiment) + '\n')
