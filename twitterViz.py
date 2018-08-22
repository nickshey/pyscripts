#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:19:50 2018

@author: nojan
"""

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials # Loads 'twitter_credentials.py'
import json  # This library used below
import webbrowser
import sys

#%%

#Code provided by teacher in STAT1559 class

###### TWITTER CLIENT ######
class TwitterClient():
    '''
    Class for using twitter client to access tweets of desired users
    '''
    def __init__(self, twitter_user=None, filename=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user
        self.filename = filename

    # This function is used pull the most recent tweets from a user's timeline
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    # This function is used to extract the friends list of a certain user
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    # This function extracts the home timeline tweets of a given user
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

    # This function can be used to write the extracted tweets to a text file
    def write_to_file(self, object_to_write, overwrite=True):
        if overwrite:
            with open(self.filename, 'w') as file:
                file.write(object_to_write + '\n')
                file.close()
        else:
            with open(self.filename, 'a') as file:
                file.write(object_to_write + '\n')
                file.close()
            return file

###### TWITTER AUTHENTICATOR ######
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

###### TWITTER STREAMER ######
class TwitterStreamer():
    '''
    Class for streaming and processing live tweets
    '''
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    def stream_tweets(self, fetched_tweets_filename, tweet_limit, hash_tag_list):
        # This handles twitter authentications and the connection to the twitter streaming API
        listener = TwitterListener(fetched_tweets_filename, tweet_limit)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        # Grabs the tweets containing the desired strings
        stream.filter(track=hash_tag_list)

###### TWITTER LISTENER ######
class TwitterListener(StreamListener):
    """
    Basic Listener Class that just prints received tweets to stdout
    """

    def __init__(self, fetched_tweets_filename, tweet_limit):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.counter = 0
        self.limit = tweet_limit
        open(self.fetched_tweets_filename, 'w').close()

    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)                               # tf.write(data + '\n')
            self.counter += 1
            if self.counter < self.limit:
                print(self.counter)
                return True
            else:
                return False
        except BaseException as e:
            print('Error on data: %s' % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning false on data method in case rates limit occurs
            return False
        print(status)

#################################
        
#%%
plotly.tools.set_credentials_file(username='nickshey', api_key='sXgdL1jM0IB2YdH2ClRb')

twitter_client = TwitterClient(sys.argv[1], 'tweets.txt')
tweets = twitter_client.get_user_timeline_tweets(100000000)
overwrite = True
for tweet in tweets:
   twitter_client.write_to_file(json.dumps(tweet._json), overwrite)  # write each tweet json to the text file
   overwrite = False  # change overwrite value to append subsequent tweets to file
tweetList = []
for line in open('tweets.txt', 'r'): # Open the file of tweets
    tweetList.append(json.loads(line))  # Add to 'tweetlist' after converting
    
#%%
filtered = list(filter(lambda tweet: "RT @" not in tweet["text"], tweetList))
tweetDf = pd.DataFrame(filtered)

trace1 = go.Bar(x=np.arange(len(tweetDf)),
            y=tweetDf["favorite_count"],
            text=tweetDf["text"],
            name="Favorites")
trace2 = go.Bar(x=np.arange(len(tweetDf)),
            y=tweetDf["retweet_count"],
            text=tweetDf["text"],
            name="Retweets")
data = [trace1,trace2]
layout= go.Layout(barmode="stack")

fig = go.Figure(data=data,layout=layout)    

url = py.iplot(fig)
url = url.resource
webbrowser.open(url)