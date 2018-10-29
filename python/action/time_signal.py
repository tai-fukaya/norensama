#-*-coding:utf-8-*-
import time

from action_base import ActionBase

class TimeSignal(ActionBase):

    REST_DURATION = 40 * 60.

    SIGNAL_MAP = {
        9: { 'text': '9時じゃ', 'isDone': False },
        10: { 'text': '10時じゃ', 'isDone': False },
        11: { 'text': '11時じゃ', 'isDone': False },
        12: { 'text': '12時じゃ', 'isDone': False },
        13: { 'text': '13時じゃ', 'isDone': False },
        14: { 'text': '14時じゃ', 'isDone': False },
        15: { 'text': '15時じゃ', 'isDone': False },
        16: { 'text': '16時じゃ', 'isDone': False },
        17: { 'text': '17時じゃ', 'isDone': False },
        18: { 'text': '18時じゃ', 'isDone': False },
        19: { 'text': '19時じゃ', 'isDone': False },
        20: { 'text': '20時じゃ', 'isDone': False },
        21: { 'text': '21時じゃ', 'isDone': False },
        22: { 'text': '22時じゃ', 'isDone': False },
    }

    def __init__(self, speaker):
        super(TimeSignal, self).__init__(speaker)
        self._next = self.SIGNAL_MAP[9]

    def check(self, data):
        if data["now"] - self._last_running_time < self.REST_DURATION:
            return False
        signal = self.SIGNAL_MAP.get(data["datetime"].hour)
        if not signal:
            return False
        ret = signal.get("isDone", True)
        if not ret:
            self._next = signal
            if data["datetime"].minute > 10:
                return False
        return not ret

    def run(self, data):
        self._sp.say(self._next["text"])
        self._next["isDone"] = True
        time.sleep(1.)
        self._last_running_time = time.time()

        return self._next["text"]
