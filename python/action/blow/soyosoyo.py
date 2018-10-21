#-*-coding:utf-8-*-
import random
import time

from action.action_base import ActionBase

class Soyosoyo(ActionBase):

    SERIFS = [
        {"name": "soyosoyo", "text": "そよそよ"},
        {"name": "sawasawa", "text": "さわさわ"},
    ]

    def __init__(self, speaker):
        super(Soyosoyo, self).__init__(speaker)

    def check(self, data):
        return abs(data.get("accelerometer").acc_x) < .4

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif["name"])
        time.sleep(.5)

        return serif["text"]
        