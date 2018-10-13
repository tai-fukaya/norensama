#-*-coding:utf-8-*-
import random
import threading
import time

import _secret as config
from speaker import Speaker
from twitter import Twitter
from action import Yureyure

class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._twitter = Twitter({
            "consumer_key": config.TWITTER_CONSUMER_KEY,
            "consumer_secret": config.TWITTER_CONSUMER_SECRET,
            "access_token": config.TWITTER_ACCESS_TOKEN,
            "access_token_secret": config.TWITTER_ACCESS_TOKEN_SECRET
        })
        self._actions = [
            Yureyure(self._speaker, self._twitter)
        ]
    
    def main(self):
        print("main")
        while True:
            data = {}
            runable_action = [x for x in self._actions if x.check(data)]
            if runable_action:
                start = time.time()
                idx = int(random.random()*len(runable_action))
                runable_action[idx].run()
                print(time.time() - start)
            time.sleep(1.)

if __name__ == "__main__":
    noren = Norensama()
    noren.main()
