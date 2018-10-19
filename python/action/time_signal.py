#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class TimeSignal(ActionBase):

    REST_DURATION = 60.

    SIGNAL_MAP = {
        9: { 'file': '9ji', 'text': '9時じゃ', 'isDone': False },
        10: { 'file': '10ji', 'text': '10時じゃ', 'isDone': False },
        11: { 'file': '11ji', 'text': '11時じゃ', 'isDone': False },
        12: { 'file': '12ji', 'text': '12時じゃ', 'isDone': False },
        13: { 'file': '13ji', 'text': '13時じゃ', 'isDone': False },
        14: { 'file': '14ji', 'text': '14時じゃ', 'isDone': False },
        15: { 'file': '15ji', 'text': '15時じゃ', 'isDone': False },
        16: { 'file': '16ji', 'text': '16時じゃ', 'isDone': False },
        17: { 'file': '17ji', 'text': '17時じゃ', 'isDone': False },
        18: { 'file': '18ji', 'text': '18時じゃ', 'isDone': False },
        19: { 'file': '19ji', 'text': '19時じゃ', 'isDone': False },
        20: { 'file': '20ji', 'text': '20時じゃ', 'isDone': False },
        21: { 'file': '21ji', 'text': '21時じゃ', 'isDone': False },
        22: { 'file': '22ji', 'text': '22時じゃ', 'isDone': False },
    }

    def __init__(self, speaker):
        super(TimeSignal, self).__init__(speaker)
        self._next = self.SIGNAL_MAP[9]

    def check(self, data):
        signal = self.SIGNAL_MAP[data["datetime"].hour]
        ret = signal["isDone"]
        if not ret:
            self._next = signal
            self.SIGNAL_MAP[data["datetime"].hour]["isDone"] = True
        return not ret

    def run(self, data):
        self._sp.say(self._next["file"])
        time.sleep(1.)

        return self._next["text"]
