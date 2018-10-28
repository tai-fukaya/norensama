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

    def get_hourly_weather(self):
        hourly = FIOHourly.FIOHourly(self.fio)
        return hourly.data[2].get('icon')

    def get_hourly_temperature(self):
        hourly = FIOHourly.FIOHourly(self.fio)
        return int(hourly.data[2].get('temperature'))

    def get_tommorow_weather(self):
        daily = FIODaily.FIODaily(self.fio)
        return daily.data[0].get('icon')


    # def get_current_humidity(self):
    #     current = FIOCurrently.FIOCurrently(self.fio)
    #     return int(float(current.humidity)*100),'%'
    # #
    # def get_current_precipProbability(self):
    #     current = FIOCurrently.FIOCurrently(self.fio)
    #     return int(float(current.precipProbability)*100),'%'
