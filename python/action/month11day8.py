#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day8(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "11月8日木曜日じゃ。",
    ]

    def __init__(self, speaker):
        super(Month11day8, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月8日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
