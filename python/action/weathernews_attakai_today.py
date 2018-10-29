#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeathernewsAttakaiToday(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "今日はこれからあったかくなりそうじゃ。",
    ]

    def __init__(self, speaker):
        super(WeathernewsAttakaiToday, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #数時間後暖かくなる場合

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
