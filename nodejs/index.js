/**
 * 人感センサーを取得する
 * 人が通ったら、一定期間、LEDを光らせる
 */
require('date-utils');
const express = require('express');
const serveIndex = require('serve-index');
const WebSocketClient = require('websocket').w3cwebsocket;
const osc = require('node-osc');
const Obniz = require('obniz');

const config = require('./_secret');

class MotionSensorObniz {
    constructor(sensor_id, obniz_id, access_token) {
        this.sensor_id = sensor_id;
        if (access_token) {
            this.obniz = new Obniz(obniz_id, {access_token: access_token});
        } else {
            this.obniz = new Obniz(obniz_id);
        }
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
                let message = `${this.sensor_id},`;
                for (let i in this.statuses) {
                    message += `${i}:${this.statuses[i]},`;
                }
                console.log(message);

                if (this.wsc.readyState !== this.wsc.CLOSED) {
                    let now = new Date();
                    this.wsc.send(["motion", this.sensor_id, position, "start", now.getTime()].join(","));
                }
                let oscmessage = new osc.Message("/motion");
                oscmessage.append(this.sensor_id);
                oscmessage.append(position);
                oscmessage.append("start");
                oscClient.send(oscmessage);
            }

            timer = setTimeout(() => {
                // TODO 停止送信
                this.statuses[position] = "0";
                let message = `${this.sensor_id},`;
                for (let i in this.statuses) {
                    message += `${i}:${this.statuses[i]},`;
                }
                console.log(message);

                if (this.wsc.readyState !== this.wsc.CLOSED) {
                    let now = new Date();
                    this.wsc.send(["motion", this.sensor_id, position, "stop", now.getTime()].join(","));
                }
                let oscmessage = new osc.Message("/motion");
                oscmessage.append(this.sensor_id);
                oscmessage.append(position);
                oscmessage.append("stop");
                oscClient.send(oscmessage);
                timer = null;
            }, 1000);
        };
    }
}

// ローカルサーバーを立ち上げて、ここでウェブソケットで通信する
const app = express();
app.use(express.static(__dirname + '/server'));
app.use(serveIndex(__dirname + '/server', {icons: true}));
const PORT = 8000;
app.listen(PORT);

let ip = process.argv[2] || '127.0.0.1';

let client = new WebSocketClient(`ws://${ip}:6700`);
let oscClient = new osc.Client("127.0.0.1", 12000);

// 店舗案内側
let mo0 = new MotionSensorObniz(
    0,
    "8894-3916",
    config.OBNIZ_ACCESS_TOKEN_88943916
);
mo0.start(client, [{
    gnd: 6, signal: 7, vcc: 8
}, {
    gnd: 3, signal: 4, vcc: 5
}, {
    gnd: 0, signal: 1, vcc: 2
}]);

// 入り口側
let mo1 = new MotionSensorObniz(
    1,
    "8972-1856"
);
mo1.start(client, [{
    gnd: 0, signal: 2, vcc: 1
}, {
    gnd: 3, signal: 5, vcc: 4
}, {
    gnd: 6, signal: 8, vcc: 7
}]);

// accelerometer
let acc0 = new Obniz("6364-1751");

acc0.onconnect = async () => {
    console.log('connect');
    let sensor = acc0.wired("KXR94-2050", {vcc:0, gnd:1, x:2, y:3, z:4 });
    sensor.onChange = values => {
        // 0.7 ~ -1.4
        let x = values.x;
        let y = values.y;
        let z = values.z;

        // console.log(`${x.toFixed(3)},${y.toFixed(3)},${z.toFixed(3)}`);
        if (client.readyState !== client.CLOSED) {
            client.send(["acc", 0, x, y, z].join(","));
        }
        let message = new osc.Message("/acc");
        message.append(x);
        message.append(y);
        message.append(z);
        oscClient.send(message);
    };
}

acc0.onclose = async () => {

}
