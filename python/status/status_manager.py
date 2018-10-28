#-*-coding:utf-8-*-
from datetime import datetime
import time

import threading
from websocket_server import WebsocketServer


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
        self._serif_names = []
        self._now = time.time()
        self._datetime_now = datetime.now()
        self._acc = Accelerometer()
        self._motion = [0, 0]

        # 一定期間分のデータを保持する
        self._motions = [0, 0]
        self._motion_logs = [[],[]]
        self._motion_statuses = [0, 0] # 0: no one, 1: enter, 2: out, 3:exist

        # 加速度のデータ
        self._accel_logs = [[], []]

        self._force_serif = ""
        self._force_action = ""

        self._server = WebsocketServer(host='127.0.0.1', port=6700)
        self._server.set_fn_new_client(self.new_client)
        self._server.set_fn_client_left(self.client_left)
        self._server.set_fn_message_received(self.message_received)

        for i in range(100):
            self._motion_logs[0].append(0)
            self._motion_logs[1].append(0)
            self._accel_logs[0].append(0)
            self._accel_logs[1].append(0)
            
    def new_client(self, client, server):
        print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
    
    def client_left(self, client, server):
        print('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

    def message_received(self, client, server, message):
        # print(message)
        data = message.split(",")
        if data[0] == 'motion':
            motion_sensor_id = int(data[1])
            status = data[3]
            self._motion[motion_sensor_id] = 0 if status == 'stop' else 1
            # TODO センサーごとに、人が入ってきた、出てきた、人がいる、人がいない状況をとる
        elif data[0] == 'acc':
            self._acc.acc_x = float(data[3])
            self._acc.acc_y = float(data[2])
            self._acc.acc_z = float(data[4])
            # TODO 基本、z軸だけでいいはず。一定期間の最低値と最高地、平均値、その差をとる
        elif data[0] == 'serif_list':
            server.send_message(client, ",".join(self._serif_names))
        elif data[0] == 'serif':
            self._force_serif = data[1]
        else:
            print(message)
    
    def update(self):

        ws_thread = threading.Thread(target=self._server.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

        while True:
            self._now = time.time()
            self._datetime_now = datetime.now()
            # TODO 天気情報

            # TODO 強制実行アクション取得
            
            time.sleep(.1)

    def get_data(self):
        force_serif = self._force_serif
        force_action = self._force_action
        self._force_action = None
        self._force_serif = None

        return {
            "now": self._now,
            "datetime": self._datetime_now,
            "accelerometer": self._acc,
            "motions": self._motion,
            "force_serif": force_serif,
            "force_action": force_action
        }

    def set_serif_names(self, names):
        self._serif_names = names
