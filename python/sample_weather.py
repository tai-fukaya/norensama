#-*-coding:utf-8-*-

from weather import Weather
import _secret as config

weather = Weather({
    "api_key": config.WEATHER_APIKEY
})

weather.get_weather()
weather.get_temperature()
weather.get_humidity()
weather.get_precipProbability()
