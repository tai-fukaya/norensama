#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class Yureyure(ActionBase):

    REST_DURATION = 60.

    def __init__(self, speaker, ifttt):
        super(Yureyure, self).__init__(speaker,ifttt)

    def check(self, data):
        return data["now"] - self._last_running_time > self.REST_DURATION \
            and abs(data.get("accelerometer").acc_z) > .5

    def run(self, data):
        self._ift.tweet("へっくし")
        self._sp.say("achoo")
        time.sleep(1.)
        self._last_running_time = time.time()
