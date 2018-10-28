#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerIkku(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "閑さや、コレドにそんな、ものはない",
        "秋雨を、あつめて早し、日本橋川（字余り）",
        "秋深き、隣はいつもの、暖簾じゃぞ",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerIkku, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターでこんにちはと言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
