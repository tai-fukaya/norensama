#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Month11day9(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "11月9日金曜日じゃ。",
        "今日のレストラン営業は、21_00までじゃ",
        "明日のTOHOシネマの営業は、11_00からじゃ",
        "明日のショップ、レストランの営業は、12_00からじゃ",
    ]

    def __init__(self, speaker):
        super(Month11day9, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #11月9日

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
