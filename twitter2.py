import tweepy
from time import sleep
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

subj = ''

api = tweepy.API(auth)

def get_Tweets():
	tweetCount = 0
	temp_tweets = []
	return_tweets = []
	print(str(tweetCount))
	while tweetCount < 25:
		api_tweets = api.search(subj,lang='en')
		temp_tweets.append(api_tweets)
		#print(return_tweets)
		for returns in temp_tweets:
			tweetCount = tweetCount + 1
		print("Stored Tweets: " + str(tweetCount))
		sleep(5)
	return return_tweets

count = 0
analysis_total = 0

public_tweets = get_Tweets()
for tweet in public_tweets:
	count = count + 1 
	analysis = TextBlob(tweet.text)
	analysis_total = analysis_total + analysis.sentiment.polarity
	print(20*'-' + '\n')
	print(tweet.text)
	print('\n' + str(analysis.sentiment) + '\n')
	print("\n Tweets Collected: " + str(count))
sleep(10)

analysis_average = analysis_total / count
analysis_average = analysis_average * 100
analysis_average = round(analysis_average,2)

if analysis_average < 0:
	pn = "NEG"
elif analysis_average > 0:
	pn = "POS"
else:
	pn = "NEU"

print('Subject: ' + subj.title())
print('Overall Sentiment: ' + str(analysis_average) + "% " + pn)
