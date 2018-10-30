#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class GreetingCommuter(ActionBase):

    REST_DURATION = 60.
    SERIFS = [
        "通勤のみなさん、いつもご苦労様じゃ", # 11時前、出た、入った
    ]

    def __init__(self, speaker):
        super(GreetingCommuter, self).__init__(speaker)

    def check(self, data):
        # 11時前、出た、入った
        duration = data["now"] - self._last_running_time
        hour = data["datetime"].hour
        is_out_or_in = sum(data["motions"]) > 0

        return duration > self.REST_DURATION and hour < 11 and is_out_or_in and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
