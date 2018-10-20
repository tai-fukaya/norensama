#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Hello(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        {"name": "ohayo", "text": "おはよう"},
        {"name": "himade", "text": "暇で忙しいのだ"},
        {"name": "curtain", "text": "孫がカーテンと、喧嘩してのぅ"},
        {"name": "mierunoka", "text": "私が見えるのか"},
        {"name": "coredosaiko", "text": "COREDOサイコー！"},
        {"name": "kiduitara", "text": "気づいたら、暖簾になっておった"},
        {"name": "fukutoku", "text": "福徳神社には、寄ったかのう？"},
        {"name": "bigbig", "text": "この暖簾、日本で一番大きいのじゃ"},
        {"name": "damaru", "text": "わかった、黙る。0.5秒黙る。"},
        {"name": "ainikite", "text": "世界中から、わしに会いに来ないかのう"},
        {"name": "ashi", "text": "足生えて、こんかなぁ！"},
    ]

    def __init__(self, speaker):
        super(Hello, self).__init__(speaker)

    def check(self, data):
        mot = data.get("motions")
        return sum(mot) > 0

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif["name"])
        time.sleep(1.)
        self._last_running_time = time.time()
        return serif["text"]
