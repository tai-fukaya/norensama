#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class DaySorry(ActionBase):

    REST_DURATION = 10. * 60.
    SERIFS = [
        "開店が遅れてすまんのう。",
    ]

    def __init__(self, speaker):
        super(DaySorry, self).__init__(speaker)

    def check(self, data):
        duration = data["now"] - self._last_running_time
        day = data["datetime"].day
        hour = data["datetime"].hour
        return day in [10, 11] and hour < 13 and duration > self.REST_DURATION and random.random() > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
