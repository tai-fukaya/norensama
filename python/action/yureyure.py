#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class Yureyure(ActionBase):

    REST_DURATION = 60.

    def __init__(self, speaker):
        super(Yureyure, self).__init__(speaker)

    def check(self, data):
        return data["now"] - self._last_running_time > self.REST_DURATION \
            and abs(data.get("accelerometer").acc_x) > .4

    def run(self, data):
        self._sp.say("へっくし")
        time.sleep(1.)
        self._last_running_time = time.time()

        return "へっくし"
        