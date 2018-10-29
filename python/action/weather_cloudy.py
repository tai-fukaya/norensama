#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeatherCloudy(ActionBase):

    REST_DURATION = 10 * 60.
    SERIFS = [
        "お日さんが雲に隠れてしまうかものう",
    ]

    def __init__(self, speaker):
        super(WeatherCloudy, self).__init__(speaker)

    def check(self, data):
        #数時間後曇りになる場合
        duration = data["now"] - self._last_running_time
        current_weather = data["weather"]["current_weather"]
        two_hour_weather = data["weather"]["two_hour_weather"]
        return duration > self.REST_DURATION and current_weather != two_hour_weather and "cloudy" in two_hour_weather

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
