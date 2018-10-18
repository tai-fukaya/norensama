#-*-coding:utf-8-*-
import random
import threading
import time

import _secret as config
# StatusManager
from status import StatusManager

from speaker import Speaker
from twitter import Twitter
from ifttt import Ifttt
# Action
from action import Yureyure, Hello, Joke


class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._twitter = Twitter({
            "consumer_key": config.TWITTER_CONSUMER_KEY,
            "consumer_secret": config.TWITTER_CONSUMER_SECRET,
            "access_token": config.TWITTER_ACCESS_TOKEN,
            "access_token_secret": config.TWITTER_ACCESS_TOKEN_SECRET
        })
        self._ifttt = Ifttt({
            "api_key": config.IFTTT_APIKEY
        })

        self._status = StatusManager()
        self._actions = [
            Yureyure(self._speaker, self._ifttt),
            Hello(self._speaker, self._ifttt),
            Joke(self._speaker, self._ifttt)
        ]
    
    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()

        while True:
            data = self._status.get_data()
            # 10分に一回、ゆれの音を決める

            # 1分間は、揺れに合わせて、ゆらゆら言っている
            start = time.time()
            while time.time() - start < 10.:
                if random.random() > .4:
                    self._speaker.say("yurayura_v80")
                elif random.random() > .3:
                    self._speaker.say("yurayura_v100")
                else:
                    self._speaker.say("yurayurayurayuura_v100")
                # 強制起動もここでやる
                
                # RT、フォロー、された場合は、ここでいう

                time.sleep(5.)
            # このタイミングで、反応があると、ちがうこともいう
            runable_action = [x for x in self._actions if x.check(data)]
            if runable_action:
                start = time.time()
                idx = int(random.random()*len(runable_action))
                runable_action[idx].run({})
                print(time.time() - start)
            time.sleep(1.)

if __name__ == "__main__":
    noren = Norensama()
    noren.main()
