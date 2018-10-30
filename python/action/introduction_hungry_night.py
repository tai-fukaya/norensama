#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class IntroductionHungryNight(ActionBase):

    REST_DURATION = 5. * 60.
    SERIFS = [
        "オイラは肉がくいたいんじゃ", # 19:00、人がいる
        "夜なのに、こんなまぶしい。なんてこったい。", # 19:00、人がいる
        "コレド室町は、和食～洋食まで何でもあるんじゃ", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラはパスタじゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラはラーメンじゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラは寿司じゃ。", # 19:00、人がいる
        "今日は何が食べたい気分じゃ？オイラは漬物じゃ。", # 19:00、人がいる
    ]

    def __init__(self, speaker):
        super(IntroductionHungryNight, self).__init__(speaker)

    def check(self, data):
        # 19時以降、人がいる
        duration = data["now"] - self._last_running_time
        hour = data["datetime"].hour
        is_exist = [x for x in data["tracking"] if x.get("status") > 0]

        return duration > self.REST_DURATION and hour >= 19 and is_exist and random.random() > .6

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
