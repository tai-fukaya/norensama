#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoIntroductionLunch(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "おなかすいたんじゃ",
        "お腹すいたのぅ、のれんはくわねど高楊枝じゃ",
        "ごはんたべにきたんか？",
        "ランチ何にする？",
        "コレド室町は、和食～洋食まで何でもあるんじゃ",
        "今日は何が食べたい気分じゃ？オイラはパスタじゃ。",
        "今日は何が食べたい気分じゃ？オイラはラーメンじゃ。",
        "今日は何が食べたい気分じゃ？オイラは寿司じゃ。",
        "今日は何が食べたい気分じゃ？オイラは漬物じゃ。",
        


    ]

    def __init__(self, speaker):
        super(CoredoIntroductionLunch, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #１１時３０分〜13時＋人がいる時

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
