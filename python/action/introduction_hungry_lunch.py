#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class IntroductionHungryLunch(ActionBase):

    REST_DURATION = 3. * 60.
    SERIFS = [
        "お腹すいたのぅ、のれんはくわねど高楊枝じゃ", # 11:30 - 13:00 人がいる、0入った
        "ごはんたべにきたんか？", # 11:30 - 13:00 人がいる、0入った
        "ランチ何にする？", # 11:30 - 13:00 人がいる、0入った
        "コレド室町は、和食～洋食まで何でもあるんじゃ", # 11:30 - 13:00 人がいる、0入った
        "今日は何が食べたい気分じゃ？オイラはパスタじゃ。", # 11:30 - 13:00 人がいる、0入った
        "今日は何が食べたい気分じゃ？オイラはラーメンじゃ。", # 11:30 - 13:00 人がいる、0入った
        "今日は何が食べたい気分じゃ？オイラは寿司じゃ。", # 11:30 - 13:00 人がいる、0入った
        "今日は何が食べたい気分じゃ？オイラは漬物じゃ。", # 11:30 - 13:00 人がいる、0入った
    ]

    def __init__(self, speaker):
        super(IntroductionHungryLunch, self).__init__(speaker)

    def check(self, data):
        # 11:00 - 13:00、人がいる
        duration = data["now"] - self._last_running_time
        hour = data["datetime"].hour
        is_exist = [x for x in data["tracking"] if x.get("status") > 0]

        return duration > self.REST_DURATION and hour >= 11 and hour < 13 and is_exist and random.random() > .6

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
