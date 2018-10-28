#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerSize(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "オイラはおっきいぞう。高さは2メートル、横幅は5mmもあるんじゃ。ひょっとしたら日本で一番大きいんじゃなかろうな",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerSize, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターで大きさはと言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
