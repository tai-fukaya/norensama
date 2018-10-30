#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class HelloDoor(ActionBase):

    # 1min
    REST_DURATION = 60.
    SERIFS = [
        "うえ!うえ!ここじゃよー",
        "みんなのれんが喋っているとは、思わんじゃろーなー",
        "この下をくぐったら、コレドじゃ！",
        "にんべんさんのだしいい匂いー！",
        "コレドサイコー",
    ]

    def __init__(self, speaker):
        super(HelloDoor, self).__init__(speaker)

    def check(self, data):
        # 入り口側、人が入る
        duration = data["now"] - self._last_running_time
        is_in = data["motions"][1] == 1

        return duration > self.REST_DURATION and is_in and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
