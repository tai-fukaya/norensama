require('date-utils');
const Obniz = require('obniz');
const WebSocketClient = require('websocket').w3cwebsocket;

const config = require('./_secret');

class MotionSensorObniz {
    constructor(sensor_id, obniz_id, access_token) {
        this.sensor_id = sensor_id;
        this.obniz = new Obniz(obniz_id, {access_token: access_token});
        this.sensors = [];
        this.statuses = [];
    }
    start(wsc, configs) {
        this.wsc = wsc;
        this.obniz.onconnect = async () => {
            for (let i in configs) {
                let config = configs[i];
                this.statuses.push("");
                let sensor = this.obniz.wired("PaPIRsVZ", config);
                sensor.onchange = this.onChange(i);
                this.sensors.push(sensor);
            }
        };
    }
    onChange(position) {
        let timer = null;
        return val => {
            // false の場合は、捨てる
            if (!val) {
                return;
            }
            
            if (timer) {
                clearTimeout(timer);
                timer = null;
            } else {
                // TODO 開始送信
                this.statuses[position] = "1";
                let message = "";
                for (let i in this.statuses) {
                    message += `${i}:${this.statuses[i]},`;
                }
                console.log(message);

                if (this.wsc.readyState !== this.wsc.CLOSED) {
                    let now = new Date();
                    this.wsc.send(["motion", this.sensor_id, position, "start", now.toFormat('YYYYMMDDHH24MISS')].join(","));
                }
            }

            timer = setTimeout(() => {
                // TODO 停止送信
                this.statuses[position] = "0";
                let message = "";
                for (let i in this.statuses) {
                    message += `${i}:${this.statuses[i]},`;
                }
                console.log(message);

                if (this.wsc.readyState !== this.wsc.CLOSED) {
                    let now = new Date();
                    this.wsc.send(["motion", this.sensor_id, position, "stop", now.toFormat('YYYYMMDDHH24MISS')].join(","));
                }
                timer = null;
            }, 1000);
        };
    }
}

let client = new WebSocketClient('ws://localhost:6700');

let mo0 = new MotionSensorObniz(
    0,
    "8894-3916",
    config.OBNIZ_ACCESS_TOKEN_88943916
);

mo0.start(client, [{
    gnd: 0, signal: 1, vcc: 2
}, {
    gnd: 3, signal: 4, vcc: 5
}, {
    gnd: 6, signal: 7, vcc: 8
}]);


/*

Sの直後に、Sじゃない場合、チェックする
000 S
100 O
010 S
001 I
012 I
021 O
120 I
102 I
210 O
201 O
123 I
132 I
213 O
231 O
312 I
321 O

*/
