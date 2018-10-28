#-*-coding:utf-8-*-
import random
import time

from action.action_base import ActionBase

class Yurayura(ActionBase):

    SERIFS = [
        "ゆらり",
        "ゆらりゆらり",
        "ゆらゆら",
    ]

    def __init__(self, speaker):
        super(Yurayura, self).__init__(speaker)

    def check(self, data):
        return data.get("accelerometer").get("status", 0) == 1

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(.5)

        return serif
        