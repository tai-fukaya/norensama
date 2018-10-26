#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Hello(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "おはよう",
        "暇で忙しいのだ",
        "孫がカーテンと、喧嘩してのぅ",
        "私が見えるのか",
        "COREDOサイコー！",
        "気づいたら、暖簾になっておった",
        "福徳神社には、寄ったかのう？",
        "この暖簾、日本で一番大きいのじゃ",
        "わかった、黙る。0.5秒黙る。",
        "世界中から、わしに会いに来ないかのう",
        "足生えて、こんかなぁ！",
    ]

    def __init__(self, speaker):
        super(Hello, self).__init__(speaker)

    def check(self, data):
        mot = data.get("motions")
        return sum(mot) > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif) # FIXME TypeError: string indices must be integers, not str
        time.sleep(1.)
        self._last_running_time = time.time()
        
        return serif
