#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeatherRainyTomorrow(ActionBase):

    REST_DURATION = 30 * 60.
    SERIFS = [
        "明日の天気は、雨じゃ。たぶん。",
    ]

    def __init__(self, speaker):
        super(WeatherRainyTomorrow, self).__init__(speaker)

    def check(self, data):
        #明日雨が降る場合
        duration = data["now"] - self._last_running_time
        tommorow_weather = data["weather"]["tommorow_weather"]

        return duration > self.REST_DURATION and "rain" in tommorow_weather and random.random() > .5

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
