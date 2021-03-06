#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterSize(ActionBase):

    # 1min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "オイラはおっきいぞう。高さは2メートル、横幅は5mmもあるんじゃ。ひょっとしたら日本で一番大きいんじゃなかろうな",
    ]

    def __init__(self, speaker):
        super(TwitterSize, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time
        search_results = [x for x in ["大きさ", "おおきさ", "身長", "デカイ", "おおきい"] if x in mentions]
        #ツイッターで大きさはと言われたら
        return duration > self.REST_DURATION and len(search_results)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
