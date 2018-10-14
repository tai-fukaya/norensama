#-*-coding:utf-8-*-
import random
import threading
import time

import _secret as config
# StatusManager
from status import StatusManager

from speaker import Speaker
from twitter import Twitter
# Action
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
        self._status = StatusManager()
        self._actions = [
            Yureyure(self._speaker, self._twitter)
        ]
    
    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()
        while True:
            data = self._status.get_data()
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
