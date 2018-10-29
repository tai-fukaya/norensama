#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class FollowThankyou(ActionBase):

    REST_DURATION = 30.
    SERIFS = [
        "フォローありがとうなのじゃ", # 音だけにしたい
    ]

    def __init__(self, speaker):
        super(FollowThankyou, self).__init__(speaker)

    def check(self, data):
        return random.random() > 0
        #フォローされたら

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
