#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerAisatsu(ActionBase):

    # 5min
    REST_DURATION = 5. * 60.
    SERIFS = [
        "こんにちは",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerAisatsu, self).__init__(speaker)

    def check(self, data):
        
        return data["now"] - self._last_running_time > self.REST_DURATION
        #ツイッターでこんにちはと言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
