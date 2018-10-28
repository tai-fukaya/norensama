#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerDare(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "オイラか？オイラはのれんさまじゃ",
        "オイラは日本橋生まれ日本橋育ちじゃ",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerDare, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターでだれ？と言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
