#-*-coding:utf-8-*-

from weather import Weather
import _secret as config

weather = Weather({
    "api_key": config.WEATHER_APIKEY
})

hour = 2
day = 1
print '現在の天気:', weather.get_current_weather()
print '現在の温度:', weather.get_current_temperature()
print str(hour), '時間後の天気:', weather.get_hourly_weather(hour)
print str(hour),'時間後の温度:', weather.get_hourly_temperature(hour)
print str(day),'日後の天気:', weather.get_tommorow_weather(day)
