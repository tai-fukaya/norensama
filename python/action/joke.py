#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Joke(ActionBase):

    REST_DURATION = 120.

    def __init__(self, speaker):
        super(Joke, self).__init__(speaker)

    def check(self, data):
        return data["now"] - self._last_running_time > self.REST_DURATION \
            and random.random() > .5

    def run(self, data):
        ret = ""
        if random.random() > .5:
            ret = "のれんにのれん！"
            self._sp.say("dajare")
        else:
            ret = "肩こるなぁ。肩ないけどね。"
            self._sp.say("katakori")
        time.sleep(1.)
        self._last_running_time = time.time()
        return ret
