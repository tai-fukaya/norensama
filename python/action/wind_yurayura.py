#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WindYurayura(ActionBase):

    REST_DURATION = 2. * 60.
    SERIFS = [
        "ゆらゆら",
        "ゆらり、",
        "ゆらり、ゆらり",
    ]

    def __init__(self, speaker):
        super(WindYurayura, self).__init__(speaker)

    def check(self, data):
        # ゆらゆら
        duration = data["now"] - self._last_running_time
        wind_status = data["accelerometer"].get("status", 0)
        return duration > self.REST_DURATION and wind_status == 1 and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        self._last_running_time = time.time()

        return serif
