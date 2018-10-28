#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerGehin(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "日本橋を歩く者は上品でないとな",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerGehin, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターで下品な事を言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
