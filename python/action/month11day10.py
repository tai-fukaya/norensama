#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day10(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "11月10日土曜日じゃ。",
        "開店が遅れてすまんのう。",
        "今日のレストラン営業は、22_00までじゃ",
        "明日のTOHOシネマの営業は、10_00からじゃ",
        "未来ののれん展もあと1日じゃ。",
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
