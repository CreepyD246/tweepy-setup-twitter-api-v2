# Importing Tweepy
import tweepy

# Credentials
api_key = "INSERT API KEY HERE"
api_secret = "INSERT SECRET API KEY HERE"
bearer_token = r"INSERT BEARER TOKEN HERE"
access_token = "INSERT ACCESS TOKEN HERE"
access_token_secret = "INSERT SECRET ACCESS TOKEN HERE"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Creating a tweet to test the bot
client.create_tweet(text="Hello World")
