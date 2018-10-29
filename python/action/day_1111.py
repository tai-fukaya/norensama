#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Day1111(ActionBase):

    REST_DURATION = 50. * 60.
    SERIFS = [
        "未来ののれん展、最終日じゃ。さみしいのう。",
    ]

    def __init__(self, speaker):
        super(Day1111, self).__init__(speaker)

    def check(self, data):
        duration = data["now"] - self._last_running_time
        return duration > self.REST_DURATION and random.random() > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
