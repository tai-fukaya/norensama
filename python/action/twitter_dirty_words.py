#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterDirtyWords(ActionBase):

    # 1min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "日本橋を歩く者は上品でないとな",
    ]

    def __init__(self, speaker):
        super(TwitterDirtyWords, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time
        search_results = [x for x in ["ちん", "まん", "うんこ", "チン", "マン", "ウンコ"] if x in mentions]
        #ツイッターで下品な事を言われたら
        return duration > self.REST_DURATION and len(search_results)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
