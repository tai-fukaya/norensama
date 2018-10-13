#-*-coding:utf-8-*-
import threading
import time

import _secretkey as config
from speaker import Speaker
from twitter import Twitter

class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._twitter = Twitter({
            "consumer_key": config.TWITTER_CONSUMER_KEY,
            "consumer_secret": config.TWITTER_CONSUMER_SECRET,
            "access_token": config.TWITTER_ACCESS_TOKEN,
            "access_token_secret": config.TWITTER_ACCESS_TOKEN_SECRET
        })
    
    def main(self):
        start = time.time()
        print("main")
        self._speaker.say("yureta")
        self._twitter.tweet("ゆれた")
        print(time.time() - start)
        self._speaker.finish()

if __name__ == "__main__":
    noren = Norensama()
    noren.main()
