#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeathernewsSamuiToday(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "気温が下がって来そうじゃ。羽織るものをもったほうがええぞ。",
    ]

    def __init__(self, speaker):
        super(WeathernewsSamuiToday, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #数時間後寒くなる場合

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
