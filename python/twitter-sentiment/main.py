import tweepy
from textblob import TextBlob

consumer_key = 'o6Do65scm6Tk8yEFLiSaGwXSt'
consumer_secret = 'ZSe61nKtNTIdad6EIJbfd0QWCbpM53mrZoF6mx6pQKzfGZ6I9p'

access_token = '169475820-VjIGKk0h2rXOHqzpzxm5zJB0Bh6RAmzwWki7QK6f'
access_token_secret = 'RbtoUKpvAcQMIfIJmmkhYXaQjTMxfsiyItkPEc2lsSG2J'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


