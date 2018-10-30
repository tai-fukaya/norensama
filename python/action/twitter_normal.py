#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterNormal(ActionBase):

    # 1min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "よく聞こえんかったの〜",
    ]

    def __init__(self, speaker):
        super(TwitterNormal, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time

        if mentions:
            print("message!")
            print(mentions)
        #ツイッターでよくわからないことを言われたら
        return duration > self.REST_DURATION and len(mentions)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
