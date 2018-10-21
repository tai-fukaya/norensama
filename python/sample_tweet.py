#-*-coding:utf-8-*-

from twitter import Twitter
import _secret as config

twitter = Twitter({
    "consumer_key": config.TWITTER_CONSUMER_KEY,
    "consumer_secret": config.TWITTER_CONSUMER_SECRET,
    "access_token": config.TWITTER_ACCESS_TOKEN,
    "access_token_secret": config.TWITTER_ACCESS_TOKEN_SECRET,
})
# message = str(raw_input('>> '))
# twitter.tweet(message)
# twitter.retweet_retrive()
# twitter.follower_retrive()
# twitter.hashtag_retrive("のれんさま")
twitter.mentions_timeline()
