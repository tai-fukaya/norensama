#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TalkGuide(ActionBase):

    REST_DURATION = 2 * 60.
    SERIFS = [
        "オイラとじゃんけんせん？　じゃんけーんぽい！あ、負けじゃ",
        "オイラの話は面白いじゃろう。座布団一枚持ってきてくれんか",
        "オイラはのう、日本橋が好きなんじゃ。昔から変わらない日本らしさが感じられてのう。これからも、ずっと見守っていくのじゃ",
        "オイラはのれんさまじゃ、オイラの話に付き合ってくれんかのう",
        "オイラは猫が好きなんじゃ。昔猫好きの絵描きがおってなぁ。名前はたしか国芳とでも言ったかのう",
        "オイラも若え頃は、「宵越しの金は持たねぇ」主義じゃった",
        "オイラも日本橋クルーズに行きたいのお",
        "かまってほしいんじゃ",
        "どのお店に行くのかな？",
        # "のれん、ぱーんち",
        "そのお店はわしも行ったぞ",
        "拡散してバズらせてくれんかのう",
        # "迷える子羊たちよ",
        "待ち合わせか？",
    ]

    def __init__(self, speaker):
        super(TalkGuide, self).__init__(speaker)

    def check(self, data):
        # 案内側、人がいる
        duration = data["now"] - self._last_running_time
        is_exist = data["motions"][0] > 0

        return duration > self.REST_DURATION and is_exist and random.random() > .5

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
