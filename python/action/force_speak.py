#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class ForceSpeak(ActionBase):

    SERIF_DATA = {
        "わ":"wa",
    }

    def __init__(self, speaker):
        super(ForceSpeak, self).__init__(speaker)
        self._next_serif = {}

    def check(self, data):
        ret = False
        if data["force_serif"] in self.SERIF_DATA:
            self._next_serif = {
                "file": self.SERIF_DATA[data["force_serif"]],
                "text": data["force_serif"]
            }
            ret = True
        return ret

    def run(self, data):
        if "file" not in self._next_serif or "text" not in self._next_serif:
            return None
        self._sp.say(self._next_serif["file"])
        time.sleep(1.)
 
        return self._next_serif["text"]
        