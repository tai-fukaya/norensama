#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Day1103(ActionBase):

    REST_DURATION = 20. * 60.
    SERIFS = [
        "今日は福徳の森で日本酒祭があるんじゃ。オイラも行きたいぞ！", # 11/3 20min
    ]

    def __init__(self, speaker):
        super(Day1103, self).__init__(speaker)

    def check(self, data):
        duration = data["now"] - self._last_running_time
        return duration > self.REST_DURATION and random.random() > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
