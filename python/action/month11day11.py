#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day11(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "開店が遅れてすまんのう。", # 11/11 -13:00 10min
        "未来ののれん展、最終日じゃ。さみしいのう。", # 11/11 1h
    ]

    def __init__(self, speaker):
        super(Month11day11, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月11日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
