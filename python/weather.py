#!/usr/bin/env python
# coding: utf-8
from forecastiopy import *

NIHONBASHI = [35.686819 , 139.774212]

class Weather(object):
    def __init__(self, config):
        self.api_key = config.get("api_key")
        self.fio = ForecastIO.ForecastIO(self.api_key, latitude=NIHONBASHI[0], longitude=NIHONBASHI[1])

    def get_weather(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        icons = {
            "clear-day": "晴天",
            "clear-night": "晴天",
            "rain": "雨",
            "snow": "雪",
            "sleet": "あられ",
            "wind": "強風",
            "fog": "霧",
            "cloudy": "くもり",
            "partly-cloudy-day": "晴れ",
            "partly-cloudy-night": "晴れ"
        }
        print '天気:', icons.get(current.icon)

    def get_temperature(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        print '温度:', current.temperature, '度'

    def get_humidity(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        print '湿度:', str(float(current.humidity)*100),'%'

    def get_precipProbability(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        print '降水確率:', str(float(current.precipProbability)*100),'%'
