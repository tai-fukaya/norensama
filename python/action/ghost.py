#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Ghost(ActionBase):

    # 2 hour
    REST_DURATION = 120 * 60.
    SERIFS = [
        # "い、入れ替わってる！？",
        "オイラのゴーストが、そう囁くのよ",
        "オイラは日本橋の人びとの集合意識から生まれたひとつの人格なのじゃよ",
        "オイラは日本橋にいる全員の意識と繋がる事もできるのじゃ！",
        "この声は脳に直接響いているのじゃぞ",
        "現在、のれんネットワークアップデート中じゃ",
    ]

    def __init__(self, speaker):
        super(Ghost, self).__init__(speaker)

    def check(self, data):
        # 入り口にひとがいない、風がゆらゆら
        duration = data["now"] - self._last_running_time
        is_no_one = data["tracking"][0].get("status", 0) == 0
        wind_status = data["accelerometer"].get("status", 0)
        return duration > self.REST_DURATION and is_no_one and wind_status > 0 and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
