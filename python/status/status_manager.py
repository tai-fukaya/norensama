#-*-coding:utf-8-*-
import time

from sensor import SerialSensorManager


class StatusManager(object):

    def __init__(self):
        self._now = 0.
        self._sensors = SerialSensorManager()
        self._sensors.search(["GY-521", "Papirs-01"])
    
    def update(self):
        while True:
            self._now = time.time()
            # センサー情報
            acc1_data = self._sensors.get_data("GY-521")
            mot1_data = self._sensors.get_data("Papirs-01")
            print(acc1_data, mot1_data)

            # TODO 天気情報
            # TODO 強制実行アクション取得
            time.sleep(.1)

    def get_data(self):
        return {"now": self._now}
