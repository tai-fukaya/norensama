#-*-coding:utf-8-*-
import time

from sensor import SerialSensorManager


class Accelerometer(object):

    def __init__(self):
        self.acc_x = 0.
        self.acc_y = 0.
        self.acc_z = 0.
        self.gyro_x = 0.
        self.gyro_y = 0.
        self.gyro_z = 0.


class StatusManager(object):

    def __init__(self):
        self._now = 0.
        self._acc = Accelerometer()
        self._motion = []

        self._sensors = SerialSensorManager()
        self._sensors.search(["GY-521", "Papirs-01"])
    
    def update(self):
        while True:
            self._now = time.time()
            # センサー情報
            acc1_data = self._sensors.get_data("GY-521")
            mot1_data = self._sensors.get_data("Papirs-01")
            print(acc1_data, mot1_data)
            if len(acc1_data) == 6:
                self._acc.acc_x = float(acc1_data[0])
                self._acc.acc_y = float(acc1_data[1])
                self._acc.acc_z = float(acc1_data[2])
            if len(mot1_data) == 1 and len(mot1_data[0]) > 0:
                self._motion.append(int(mot1_data[0]))
                self._motion = self._motion[-20:]

            # TODO 天気情報
            # TODO 強制実行アクション取得
            time.sleep(.1)

    def get_data(self):
        return {"now": self._now, "accelerometer": self._acc, "motions": self._motion}
