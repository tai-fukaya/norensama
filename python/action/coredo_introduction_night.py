#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoIntroductionNight(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "オイラは肉がくいたいんじゃ", # 19:00、人がいる
        "おつかれさま", # 19:00、1 人がでてく
        "おやすみー", # 19:00、1 人がでてく
        "お仕事お疲れ様じゃ、身体を休めるのも大事じゃぞ", # 19:00、人がでてく
        "夜遊びには気を付けるのじゃぞ", # 19:00、人がでてく
        "夜なのに、こんなまぶしい。なんてこったい。", # 19:00、人がいる
        "コレド室町は、和食～洋食まで何でもあるんじゃ", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラはパスタじゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラはラーメンじゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラは寿司じゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラは漬物じゃ。", # 19:00、人がいる
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
