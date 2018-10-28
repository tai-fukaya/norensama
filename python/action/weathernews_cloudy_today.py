#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeathernewsCloudyToday(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "お日さんが雲に隠れてしまうかものう",
    ]

    def __init__(self, speaker):
        super(WeathernewsCloudyToday, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #数時間後曇りになる場合

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
