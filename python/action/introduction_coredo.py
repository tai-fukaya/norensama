#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class IntroductionCoredo(ActionBase):

    REST_DURATION = 60.
    SERIFS = [
        "ＴＯＨＯシネマはエスカレーターで２階に上がって突き当りじゃ", # 0,1, はいった
        "ここは、コレド室町1じゃ", # 0,1 はいった
        "コレドは『日本を賑わす日本橋』がテーマなんじゃ", # 0,1 入った
        "コレドはcore edoっていう意味らしいんじゃ。江戸の中心ってことじゃ", # 0,1 入った
        "コレド室町２はまっすぐ抜けた先じゃ", # 0,1 入った
        "コレド室町３は、オイラの方を向いて右手じゃ", # 0,1, 入った
        # "コレド室町1の右の暖簾はな、五街道をモチーフに作られておってだな、栄という漢字を元に、賑わいをテーマに作られた紋でな、わしもこの紋がお気に入りで、お気に入りでのう、だから、、、何じゃ？話が長いってかのう？", # 1, いる
    ]

    def __init__(self, speaker):
        super(IntroductionCoredo, self).__init__(speaker)

    def check(self, data):
        # はいった
        duration = data["now"] - self._last_running_time
        is_in = 1 in data["motions"]

        return duration > self.REST_DURATION and is_in and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
