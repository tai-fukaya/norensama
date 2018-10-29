#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterIkku(ActionBase):

    # 1min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "閑さや、コレドにそんな、ものはない",
        "秋雨を、あつめて早し、日本橋川（字余り）",
        "秋深き、隣はいつもの、暖簾じゃぞ",
    ]

    def __init__(self, speaker):
        super(TwitterIkku, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time
        search_results = [x for x in ["一句読んで", "一句よんで", "一句詠んで"] if x in mentions]
        #ツイッターで一句読んでと言われたら
        return duration > self.REST_DURATION and len(search_results)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
