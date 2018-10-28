#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoIntroductionAM9(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "通勤のみなさん、いつもご苦労様じゃ",
    ]

    def __init__(self, speaker):
        super(CoredoIntroductionAM9, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #朝9時から10時+人が通った時

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
