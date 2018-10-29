#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Day1109(ActionBase):

    REST_DURATION = 20. * 60.
    SERIFS = [
        "今日のレストラン営業は、21時までじゃ",
        "明日のTOHOシネマの営業は、11時からじゃ",
        "明日のショップ、レストランの営業は、12時からじゃ",
    ]

    def __init__(self, speaker):
        super(Day1109, self).__init__(speaker)

    def check(self, data):
        duration = data["now"] - self._last_running_time
        return duration > self.REST_DURATION and random.random() > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
