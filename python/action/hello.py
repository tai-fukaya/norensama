#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Hello(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "へいらっしゃい",
        "おはよう",
        "のれんさまぞ",

        "隣ののれんがいつものコレドののれんじゃ",
        "風によるなびきと人の行き来に反応して喋るのじゃ",
        
        "今日はお買い物かの？",
        "暇で忙しいのだ",
    ]

    def __init__(self, speaker):
        super(Hello, self).__init__(speaker)

    def check(self, data):
        # 入り口側、人が入る
        duration = data["now"] - self._last_running_time
        is_in = 1 in data["motions"]

        return duration > self.REST_DURATION and is_in and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
