#-*-coding:utf-8-*-
# https://qiita.com/bakira/items/00743d10ec42993f85eb
# https://su-gi-rx.com/archives/942#3_StreamListener
from requests_oauthlib import OAuth1Session

TWEET_POST_URL = "https://api.twitter.com/1.1/statuses/update.json"

class Twitter(object):

    def __init__(self, config):
        self.consumer_key = config.get("consumer_key")
        self.consumer_secret = config.get("consumer_secret")
        self.access_token = config.get("access_token")
        self.access_token_secret = config.get("access_token_secret")

        self._session = OAuth1Session(
            self.consumer_key,self.consumer_secret,
            self.access_token, self.access_token_secret
        )

    def tweet(self, message):
        print("tweet:{}".format(message))

        # params = {"status": message}
        # res = self._session.post(TWEET_POST_URL, params = params)
        # print(res)
