#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Byebye(ActionBase):

    # 10min
    REST_DURATION = 30.
    SERIFS = [
        "また来るんじゃよ",
        "どうしたんでい",

        "みなオイラのことを無視せんでくれ",
        "みんなが日本橋の人の良さに触れてくれるとよいなぁ",
        "福徳神社には寄ったかのう？",
        "人生には何くそ、と言う気持ちが不可欠じゃ",
        "最近の若者はきらきらしておる、負けてられんな！",
        "気づいたらのれんになっておった",
        "来世はなにになれるのかのぅ、のれんはいやじゃのう",
        "足生えてこんかなぁ",
        "季節の変わりめじゃ体には気をつけるのじゃぞ",
        "はっ！寝てしまっておったイカンイカン",
    ]

    def __init__(self, speaker):
        super(Byebye, self).__init__(speaker)

    def check(self, data):
        # ひとがでる
        duration = data["now"] - self._last_running_time
        is_out = 2 in data["motions"]

        return duration > self.REST_DURATION and is_out and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
