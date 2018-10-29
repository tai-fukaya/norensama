#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day10(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "開店が遅れてすまんのう。", # 11/10 - 13:00 10min
        "今日のレストラン営業は、22_00までじゃ", # 11/10 1h
        "明日のTOHOシネマの営業は、10_00からじゃ", # 11/10 30min
        "未来ののれん展もあと1日じゃ。", # 11/10 30min
    ]

    def __init__(self, speaker):
        super(Month11day10, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月10日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
