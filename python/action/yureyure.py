#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class Yureyure(ActionBase):

    REST_DURATION = 60.

    def __init__(self, speaker, ifttt):
        super(Yureyure, self).__init__(speaker,ifttt)

    def check(self, data):
        return data["now"] - self._last_running_time > self.REST_DURATION \
            and data.get("accelerometer").acc_z > -5000.

    def run(self, data):
        self._ift.tweet("ゆれた")
        self._sp.say("yureta")
        time.sleep(1.)
        self._last_running_time = time.time()
