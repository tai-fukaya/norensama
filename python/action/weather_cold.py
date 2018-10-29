#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeatherCold(ActionBase):

    REST_DURATION = 10 * 60.
    SERIFS = [
        "気温が下がって来そうじゃ。羽織るものをもったほうがええぞ。",
    ]

    def __init__(self, speaker):
        super(WeatherCold, self).__init__(speaker)

    def check(self, data):
        # ２時間後寒くなる
        duration = data["now"] - self._last_running_time
        current_temperature = data["weather"]["current_temperature"]
        two_hour_temperature = data["weather"]["two_hour_temperature"]
        return duration > self.REST_DURATION and current_temperature - two_hour_temperature > 3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
