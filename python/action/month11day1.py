#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day1(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "11月1日木曜日じゃ。",
    ]

    def __init__(self, speaker):
        super(Month11day1, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月１日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
