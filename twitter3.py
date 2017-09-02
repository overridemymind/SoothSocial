import tweepy
from time import sleep
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_Tweets(subj, tgtCount):
	print('\n'+20*'*')
	print('Getting Tweets. Please Stand by.')
	print(20*'*'+'\n')
	tweetCount = 0
	lastProgress = 0
	tweetIDs = []
	try:
		return_tweets = api.search(subj, lang='en')
	except tweepy.RateLimitError:
		print('Rate Limited. Stand by.')
		sleep(30)
	for initial_tweets in return_tweets:
		tweetIDs.append(initial_tweets.id)
		tweetCount = tweetCount + 1
	while tweetCount < tgtCount:
		try:
			return_tweets = api.search(subj,lang='en')
		except tweepy.RateLimitError:
			print('Rate Limited. Stand by.')
			sleep(30)
		for returns in return_tweets:
			if returns.id not in tweetIDs:
				#print(returns.id)
				tweetIDs.append(returns.id)
				return_tweets.append(returns)
				tweetCount = tweetCount + 1
		if tweetCount < tgtCount:
			progress = (tweetCount / tgtCount)*100
			if lastProgress != progress:
				lastProgress = progress
				print(str(progress) + "%  complete.")
			sleep(2)
	print(20*'*')
	print("Done.\n" + 20*'*' + "\n")
	return return_tweets

count = 0
analysis_total = 0

subject = input('Please enter your subject: ')
numTweets = input('About how many tweets? ')
public_tweets = get_Tweets(str(subject), int(numTweets))
print('Analyzing Sentiment. Please wait.\n')
for tweet in public_tweets:
	count = count + 1 
	analysis = TextBlob(tweet.text)
	analysis_total = analysis_total + analysis.sentiment.polarity
	#print(20*'-' + '\n')
	#print(tweet.text)
	#print('\n' + str(analysis.sentiment) + '\n')
	#print("\n Tweets Collected: " + str(count))

analysis_average = analysis_total / count
analysis_average = analysis_average * 100
analysis_average = round(analysis_average,2)

if analysis_average < 0:
	pn = "NEG"
elif analysis_average > 0:
	pn = "POS"
else:
	pn = "NEU"

print('Subject: ' + subject.title())
print('Overall Sentiment: ' + str(analysis_average) + "% " + pn)
