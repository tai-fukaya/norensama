#-*-coding:utf-8-*-
import time

import threading
from websocket_server import WebsocketServer
# from sensor import SerialSensorManager


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
        self._motion = [0, 0]

        self._server = WebsocketServer(host='127.0.0.1', port=6700)
        self._server.set_fn_new_client(self.new_client)
        self._server.set_fn_client_left(self.client_left)
        self._server.set_fn_message_received(self.message_received)
        # self._sensors = SerialSensorManager()
        # self._sensors.search(["GY-521", "Papirs-01"])
    
    def new_client(self, client, server):
        print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
    
    def client_left(self, client, server):
        print('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

    def message_received(self, client, server, message):
        # print(message)
        data = message.split(",")
        if data[0] == 'motion':
            motion_sensor_id = int(data[2])
            status = data[3]
            self._motion[motion_sensor_id] = 0 if status == 'stop' else 1
        elif data[0] == 'acc':
            self._acc.acc_x = float(data[2])
            self._acc.acc_y = float(data[3])
            self._acc.acc_z = float(data[4])
    
    def update(self):

        ws_thread = threading.Thread(target=self._server.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

        while True:
            self._now = time.time()
            # # センサー情報
            # acc1_data = self._sensors.get_data("GY-521")
            # mot1_data = self._sensors.get_data("Papirs-01")
            # print(acc1_data, mot1_data)
            # if len(acc1_data) == 6:
            #     self._acc.acc_x = float(acc1_data[0])
            #     self._acc.acc_y = float(acc1_data[1])
            #     self._acc.acc_z = float(acc1_data[2])
            # if len(mot1_data) == 1 and len(mot1_data[0]) > 0:
            #     self._motion.append(int(mot1_data[0]))
            #     self._motion = self._motion[-20:]

            # TODO 天気情報
            # TODO 強制実行アクション取得
            time.sleep(.1)

    def get_data(self):
        return {"now": self._now, "accelerometer": self._acc, "motions": self._motion}
