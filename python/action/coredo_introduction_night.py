#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoIntroductionNight(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "オイラは肉がくいたいんじゃ",
        "おつかれさま",
        "おやすみー",
        "お仕事お疲れ様じゃ、身体を休めるのも大事じゃぞ",
        "夜なのに、こんなまぶしい。なんてこったい。",
        "夜遊びには気を付けるのじゃぞ",
        "コレド室町は、和食～洋食まで何でもあるんじゃ",
        "今日は何が食べたい気分じゃ？オイラはパスタじゃ。",
        "今日は何が食べたい気分じゃ？オイラはラーメンじゃ。",
        "今日は何が食べたい気分じゃ？オイラは寿司じゃ。",
        "今日は何が食べたい気分じゃ？オイラは漬物じゃ。",
    ]

    def __init__(self, speaker):
        super(CoredoIntroductionNight, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #19時00分〜21時＋人がいる時

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
