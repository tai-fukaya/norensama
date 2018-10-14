#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class Yureyure(ActionBase):

    def __init__(self, speaker, twitter):
        super(Yureyure, self).__init__(speaker,twitter)

    def run(self):
        self._tw.tweet("ゆれた")
        self._sp.say("yureta")
        time.sleep(1.)
        self._last_running_time = time.time()
        