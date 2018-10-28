#-*-coding:utf-8-*-
import json
from requests_oauthlib import OAuth1Session
import sys
import time

class TwitterManager(object):

    def __init__(self, tw):
        self._twitter = tw

        self._has_retweet = False
        self._has_follower = False
        self._hashtag_messages = []
        self._mention_messages = []

        self._tweet_messages = []
    
    def update(self):
        last_retweet_time = 0.0
        last_follower_time = 0.0
        last_hashtag_time = 0.0
        last_mention_time = 0.0
        while True:
            # tweet
            tweet_messages = self._tweet_messages
            self._tweet_messages = []
            if len(tweet_messages):
                for m in tweet_messages:
                    self._twitter.tweet(m)
            # FIXME 以下、取得タイミングは調整して
            # RT 75times/15min
            if time.time() - last_retweet_time > 20.:
                # self._has_retweet = self._has_retweet or self._twitter.has_retweet()
                last_retweet_time = time.time()
            # Follower 15times/15min
            if time.time() - last_follower_time > 60.:
                # self._has_follower = self._has_follower or self._twitter.has_follower()
                last_follower_time = time.time()
            # hash 180times/15min
            if time.time() - last_hashtag_time > 10.:
                # self._hashtag_messages.extend(self._twitter.get_hashtags())
                last_hashtag_time = time.time()
            # mention ?
            if time.time() - last_mention_time > 5.:
                # self._mention_messages.extend(self._twitter.get_mention_timeline())
                last_mention_time = time.time()
            time.sleep(1.)
    
    def get_data(self):
        has_retweet = self._has_retweet
        has_follower = self._has_follower
        hashtag_messages = self._hashtag_messages
        mention_messages = self._mention_messages
        self._has_retweet = False
        self._has_follower = False
        self._hashtag_messages = []
        self._mention_messages = []

        return {
            "retweet": has_retweet,
            "follower": has_follower,
            "hashtag": len(hashtag_messages) > 0,
            "mentions": mention_messages
        }

    