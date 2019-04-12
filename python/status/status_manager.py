#-*-coding:utf-8-*-
from datetime import datetime
import time
import threading
from websocket_server import WebsocketServer

from weather import Weather
import _secret as config


class Accelerometer(object):

    def __init__(self):
        self.acc_x = 0.
        self.acc_y = 0.
        self.acc_z = 0.
        self.gyro_x = 0.
        self.gyro_y = 0.
        self.gyro_z = 0.


class StatusManager(object):

    def __init__(self, ip):
        self._ip = ip
        self._serif_names = []
        self._now = time.time()
        self._datetime_now = datetime.now()

        self._acc = Accelerometer()
        # 加速度のデータ
        self._accel_receive_data = [Accelerometer()]
        self._accel_logs = [[]]
        self._accel_z_data = [{
            "min": 0, "max": 0, "absmin": 0, "absmax": 0,
            "avg": 0, "diff": 0, "status": 0  # 0: no, 1: yurayura, 2: byubyu
        }]

        # 一定期間分のデータを保持する
        self._motion_receive_data = [[
                {"status":0, "time":0},
                {"status":0, "time":0},
                {"status":0, "time":0}
            ], [
                {"status":0, "time":0},
                {"status":0, "time":0},
                {"status":0, "time":0}
            ]]
        
        self._motion_logs = [[],[]]
        self._human_statuses = [0, 0] # 0: no_one, 1: enter, 2: out
        self._tracking_statuses = [{
            "status": 0,
            "time": 0
        }, {
            "status": 0,
            "time": 0
        }] #0:no, 1:exist

        self._force_serif = ""
        self._force_action = ""

        self._server = WebsocketServer(host=self._ip, port=6700)
        self._server.set_fn_new_client(self.new_client)
        self._server.set_fn_client_left(self.client_left)
        self._server.set_fn_message_received(self.message_received)

        # 天気情報
        self._weather = Weather({
            "api_key": config.WEATHER_APIKEY
        })
        self._weather_get_time = 0.
        self._current_weather = ""
        self._current_temperature = 15
        self._two_hour_weather = ""
        self._two_hour_temperature = 15
        self._tomorrow_weather = ""

        for _ in range(100):
            self._motion_logs[0].append(0)
            self._motion_logs[1].append(0)
            self._accel_logs[0].append(Accelerometer())
            
    def new_client(self, client, server):
        print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
    
    def client_left(self, client, server):
        print('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

    def message_received(self, client, server, message):
        # print(message)
        data = message.split(",")
        if data[0] == 'motion':
            # sensor_id, position, status, unixtime
            motion_sensor_id = int(data[1])
            position = int(data[2])
            status = data[3]
            unixtime = int(data[4])/1000.
            # print(motion_sensor_id, position, status, unixtime)
            # self._motion[motion_sensor_id] = 0 if status == 'stop' else 1
            self._motion_receive_data[motion_sensor_id][position] = {
                "status": 0 if status == 'stop' else 1,
                "time": unixtime
            }
        elif data[0] == 'acc':
            # sensor_id, x, y, z
            sensor_id = int(data[1])
            if len(self._accel_logs) <= sensor_id:
                return
            acc = Accelerometer()
            acc.acc_x = float(data[2])
            acc.acc_y = float(data[3])
            acc.acc_z = float(data[4])
            self._accel_receive_data[sensor_id] = acc
            self._accel_logs[sensor_id].append(acc)
            self._accel_logs[sensor_id] = self._accel_logs[sensor_id][-100:]
            accel_z_logs = [x.acc_z for x in self._accel_logs[sensor_id]]
            abs_accel_z_logs = [abs(x.acc_z) for x in self._accel_logs[sensor_id]]

            min_z = min(accel_z_logs)
            max_z = max(accel_z_logs)
            absmin_z = min(abs_accel_z_logs)
            absmax_z = max(abs_accel_z_logs)
            avg_z = sum(accel_z_logs)/len(accel_z_logs)
            diff_z = max_z - min_z
            status = 0
            # 強風
            if absmin_z > .35:
                status = 2
            # パタパタ
            elif abs(avg_z) < .05 and diff_z > .3 :
                status = 1

            # 基本、z軸だけでいいはず。一定期間の最低値と最高地、平均値、その差をとる
            self._accel_z_data[sensor_id] = {
                "min": min_z, "max": max_z,
                "absmin": absmin_z, "absmax": absmax_z,
                "avg": avg_z, "diff": diff_z, "status": status
            }
            
        elif data[0] == 'serif_list':
            server.send_message(client, ",".join(self._serif_names))
        elif data[0] == 'serif':
            self._force_serif = data[1].encode('utf-8')
        else:
            print(message)
    
    def update(self):

        ws_thread = threading.Thread(target=self._server.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

        while True:
            self._now = time.time()
            self._datetime_now = datetime.now()

            # モーションセンサーの状態の判定
            # TODO センサーごとに、人が入ってきた、出てきた、人がいる、人がいない状況をとる
            for i in range(2):
                current_sensor_information = self._motion_receive_data[i]
                
                prev_sensor_status = self._human_statuses[i]
                # すべて０なら、no_one
                current_status = sum([x.get("status", 0) for x in current_sensor_information])

                if current_status == 0:
                    self._human_statuses[i] = 0
                elif prev_sensor_status == 0:
                    if current_status == 1:
                        # 1つだけ、反応している
                        self._human_statuses[i] = 0
                        # # １のもののインデックス
                        # if current_sensor_information[0].get("status") == 1:
                        #     self._human_statuses[i] = 1
                        # elif current_sensor_information[2].get("status") == 1:
                        #     self._human_statuses[i] = 2
                        # else:
                        #     self._human_statuses[i] = 0
                    else:
                        self._human_statuses[i] = 1
                        # 古い順にふたつとる
                        # 古いほうのインデックスが、次のよりも大きい場合IN
                        sorted_timestamp = sorted([x.get("time", 0.) for x in current_sensor_information if x.get("status") == 1])
                        top_index = [j for j, x in enumerate(current_sensor_information) if x.get("time") == sorted_timestamp[0]]
                        second_index = [j for j, x in enumerate(current_sensor_information) if x.get("time") == sorted_timestamp[1]]
                        print(top_index, second_index, sorted_timestamp)
                        if len(top_index) and len(second_index):
                            if top_index[0] < second_index[0]:
                                self._human_statuses[i] = 2
                self._motion_logs[i].append(1 if current_status > 0 else 0)
                self._motion_logs[i] = self._motion_logs[i][-100:]
                tracking_status = 1 if sum(self._motion_logs[i]) > 5 else 0
                prev_tracking_status = self._tracking_statuses[i].get("status")
                if prev_tracking_status != tracking_status:
                    self._tracking_statuses[i] = {
                        "status": tracking_status,
                        "time": datetime.now()
                    }

            # 天気情報
            if time.time() - self._weather_get_time > 3600:
                # １時間に一回
                print("get weather")
                self._current_weather = self._weather.get_current_weather()
                self._current_temperature = self._weather.get_current_temperature()
                self._two_hour_weather = self._weather.get_hourly_weather(2)
                self._two_hour_temperature = self._weather.get_hourly_temperature(2)
                self._tomorrow_weather = self._weather.get_daily_weather(0)
                self._weather_get_time = time.time()
            time.sleep(.05)

    def get_data(self):
        force_serif = self._force_serif
        force_action = self._force_action
        self._force_action = None
        self._force_serif = None

        return {
            "now": self._now,
            "datetime": self._datetime_now,
            "accelerometer": self._accel_z_data[0],
            "motions": self._human_statuses,
            "tracking": self._tracking_statuses,
            "weather": {
                "current_weather": self._current_weather,
                "current_temperature": self._current_temperature,
                "two_hour_weather": self._two_hour_weather,
                "two_hour_temperature": self._two_hour_temperature,
                "tommorow_weather": self._tomorrow_weather
            },
            "force_serif": force_serif,
            "force_action": force_action
        }

    def set_serif_names(self, names):
        self._serif_names = names
