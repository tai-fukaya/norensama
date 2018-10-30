#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class SoLonely(ActionBase):

    # 10min
    REST_DURATION = 10 * 60.
    SERIFS = [
        "みんなのれんが喋っているとは、思わんじゃろーなー",
        "肩こるなー、肩ないけどね",
        "好きな事は好きという、そんなのれんに私はなりたい",
        "暇なんじゃ",
        "最近猫みないニャー",
    ]

    def __init__(self, speaker):
        super(SoLonely, self).__init__(speaker)

    def check(self, data):
        # ひとがいない
        duration = data["now"] - self._last_running_time
        is_no_one = len([x for x in data["tracking"] if x.get("status", 0) == 0]) > 0

        return duration > self.REST_DURATION and is_no_one and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
