#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class WeatherSunny(ActionBase):

    REST_DURATION = 10 * 60.
    SERIFS = [
        "この後は、晴れてきそうじゃ",
    ]

    def __init__(self, speaker):
        super(WeatherSunny, self).__init__(speaker)

    def check(self, data):
        #数時間後晴れになる場合
        duration = data["now"] - self._last_running_time
        current_weather = data["weather"]["current_weather"]
        two_hour_weather = data["weather"]["two_hour_weather"]
        return duration > self.REST_DURATION and current_weather != two_hour_weather and "clear" in two_hour_weather

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif
