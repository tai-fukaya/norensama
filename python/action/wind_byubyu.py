#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WindByubyu(ActionBase):

    REST_DURATION = 2. * 60.
    SERIFS = [
        "びゅーびゅー",
    ]

    def __init__(self, speaker):
        super(WindByubyu, self).__init__(speaker)

    def check(self, data):
        # びゅーびゅー
        duration = data["now"] - self._last_running_time
        wind_status = data["accelerometer"].get("status", 0)
        return duration > self.REST_DURATION and wind_status == 2 and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
