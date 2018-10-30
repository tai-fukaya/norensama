#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterFavorite(ActionBase):

    # 5min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "オイラは天ぷらが好きじゃ。でも蕎麦も好きじゃ。でも鰻も好きじゃ。いや、鮨かのう。決められんわい。",
    ]

    def __init__(self, speaker):
        super(TwitterFavorite, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time
        search_results = [x for x in ["好きな食べものは？", "なにが好き？"] if x in mentions]
        #ツイッターで、好きな食べものは？と言われたら
        return duration > self.REST_DURATION and len(search_results)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
