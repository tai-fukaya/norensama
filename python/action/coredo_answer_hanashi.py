#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class CoredoAnswerHanashi(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "暖簾の小話〜。昔は暖簾の色の使い分けは、業種によって約束事があったんじゃよ",
        "暖簾の小話〜。暖簾にもいろんな種類があっての〜、太鼓暖簾っていう、下から支えられてる暖簾もあるのじゃ。",
        "暖簾の小話〜。暖簾は、汚れているほど、繁盛しているという目安だったんじゃ。",
        "暖簾の小話〜。暖簾はのう、寒さしのぎだけじゃなく、暑さしのぎにもなるんじゃ。",
    ]

    def __init__(self, speaker):
        super(CoredoAnswerHanashi, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #ツイッターで話してと言われたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
