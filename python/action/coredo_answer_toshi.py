#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerToshi(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "オイラは500歳、じゃったかな",
        "はて、何歳じゃったかのう",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerToshi, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターで歳はと言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
