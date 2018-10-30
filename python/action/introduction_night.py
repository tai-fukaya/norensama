#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class IntroductionNight(ActionBase):

    REST_DURATION = 60.
    SERIFS = [
        "おつかれさま", # 19:00、1 人がでてく
        "おやすみー", # 19:00、1 人がでてく
        "お仕事お疲れ様じゃ、身体を休めるのも大事じゃぞ", # 19:00、人がでてく
        "夜遊びには気を付けるのじゃぞ", # 19:00、人がでてく
    ]

    def __init__(self, speaker):
        super(IntroductionNight, self).__init__(speaker)

    def check(self, data):
        # 19時以降、人が出て行く
        duration = data["now"] - self._last_running_time
        hour = data["datetime"].hour
        is_out = 2 in data["motions"]

        return duration > self.REST_DURATION and hour >= 19 and is_out

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
