#the modules you will need
import tweepy
from tweepy.auth import OAuthHandler

#Your Info here
auth = tweepy.OAuthHandler(API_key, API_secret_key)

auth.set_access_token(Acess_token, Acess_token_secret)

#creates the API     dont mess with the auth part, its meant to be there
api = tweepy.API(auth)

your_tweet = #whatever you want



#this tweets
api.update_status(your_tweet)



#if this prints in the terminal, the tweet has been tweeted
print('tweet has been tweeted')



