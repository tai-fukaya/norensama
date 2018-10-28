#!/usr/bin/env python
# coding: utf-8
from forecastiopy import *

NIHONBASHI = [35.686819 , 139.774212]

class Weather(object):
    def __init__(self, config):
        self.api_key = config.get("api_key")
        self.fio = ForecastIO.ForecastIO(self.api_key, latitude=NIHONBASHI[0], longitude=NIHONBASHI[1])

    def get_current_weather(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        return current.icon

    def get_current_temperature(self):
        current = FIOCurrently.FIOCurrently(self.fio)
        return int(current.temperature)

    def get_hourly_weather(self,hour):
        hourly = FIOHourly.FIOHourly(self.fio)
        return hourly.data[hour].get('icon')

    def get_hourly_temperature(self,hour):
        hourly = FIOHourly.FIOHourly(self.fio)
        return int(hourly.data[hour].get('temperature'))

    def get_daily_weather(self,day):
        daily = FIODaily.FIODaily(self.fio)
        return daily.data[day].get('icon')
