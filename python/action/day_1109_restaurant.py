#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Day1109Restaurant(ActionBase):

    REST_DURATION = 15. * 60.
    SERIFS = [
        "今日のレストラン営業は、21時までじゃ",
    ]

    def __init__(self, speaker):
        super(Day1109Restaurant, self).__init__(speaker)

    def check(self, data):
        duration = data["now"] - self._last_running_time
        hour = data["datetime"].hour
        return hour >= 18 and duration > self.REST_DURATION and random.random() > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
