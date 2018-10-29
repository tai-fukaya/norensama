#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Today(ActionBase):

    REST_DURATION = 50. * 60.

    SERIF_MAP = {
        1: "11月1日木曜日じゃ。",
        2: "11月2日金曜日じゃ。",
        3: "11月3日土曜日じゃ。",
        4: "11月4日日曜日じゃ。",
        5: "11月5日月曜日じゃ。",
        6: "11月6日火曜日じゃ。",
        7: "11月7日水曜日じゃ。",
        8: "11月8日木曜日じゃ。",
        9: "11月9日金曜日じゃ。",
        10: "11月10日土曜日じゃ。",
        11: "11月11日日曜日じゃ。",
        31: "10月31日水曜日じゃ。",
    }

    def __init__(self, speaker):
        super(Today, self).__init__(speaker)

    def check(self, data):
        # 30 - 40 minに動かす
        duration = data["now"] - self._last_running_time
        minute = data["datetime"].minute
        day = data["datetime"].day

        return duration > self.REST_DURATION and minute > 30 and minute < 40 and self.SERIF_MAP.has_key(day)

    def run(self, data):
        day = data["datetime"].day
        serif = self.SERIF_MAP.get(day)
        if serif:
            self._sp.say(serif)
            time.sleep(1.)
        self._last_running_time = time.time()
        return serif
