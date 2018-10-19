#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class Hello(ActionBase):

    REST_DURATION = 30.

    def __init__(self, speaker):
        super(Hello, self).__init__(speaker)

    def check(self, data):
        mot = data.get("motions")
        return sum(mot) > 0

    def run(self, data):
        self._sp.say("ohayo")
        time.sleep(1.)
        self._last_running_time = time.time()
        return "おはよう"
