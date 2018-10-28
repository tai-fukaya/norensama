#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day2(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "11月2日金曜日じゃ。",
    ]

    def __init__(self, speaker):
        super(Month11day2, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月2日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
