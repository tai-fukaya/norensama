#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TwitterWhoAreYou(ActionBase):

    # 1min
    REST_DURATION = 1. * 60.
    SERIFS = [
        "オイラか？オイラはのれんさまじゃ",
        "オイラは日本橋生まれ日本橋育ちじゃ",
    ]

    def __init__(self, speaker):
        super(TwitterWhoAreYou, self).__init__(speaker)

    def check(self, data):
        mentions = data["twitter"]["mentions"]
        duration = data["now"] - self._last_running_time
        search_results = [x for x in ["誰？", "だれ？"] if x in mentions]
        #ツイッターでだれ？と言われたら
        return duration > self.REST_DURATION and len(search_results)

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
