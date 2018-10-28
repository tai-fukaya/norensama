#-*-coding:utf-8-*-

from weather import Weather
import _secret as config

weather = Weather({
    "api_key": config.WEATHER_APIKEY
})

print '現在の天気:', weather.get_current_weather()
print '現在の温度:', weather.get_current_temperature()
print '2時間後の天気:', weather.get_hourly_weather()
print '2時間後の温度:', weather.get_hourly_temperature()
print '明日の天気:', weather.get_tommorow_weather()
