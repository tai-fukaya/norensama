/**
 * 人感センサーを取得する
 * 人が通ったら、一定期間、LEDを光らせる
 */
require('date-utils');
const express = require('express');
const serveIndex = require('serve-index');
const WebSocketClient = require('websocket').w3cwebsocket;
const Obniz = require('obniz');

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

// ローカルサーバーを立ち上げて、ここでウェブソケットで通信する
const app = express();
app.use(express.static(__dirname + '/server'));
app.use(serveIndex(__dirname + '/server', {icons: true}));
const PORT = 8000;
app.listen(PORT);
console.log(require('os').networkInterfaces().en0[1].address, PORT);
// TODO Facebook messanger にIPを流す

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

// accelerometer
let acc0 = new Obniz("6364-1751");
let accValueArray = [];

acc0.onconnect = async function () {
    console.log("connect", acc0.id);
}

acc0.repeat(async function() {
    // accelerometer
    let sensor = acc0.wired("KXR94_2050", {x: 2, y: 1, z: 0, gnd:10, vcc:11 });
    let accValues = await sensor.getWait();
    accValueArray.push(accValues);
    if (accValueArray.length > 10) {
        let begin = accValueArray.length - 10;
        accValueArray = accValueArray.slice(begin);
    }
    let count = 0;
    let averageAccValues = {x: 0, y: 0, z:0};
    for (let acc of accValueArray) {
        if (isNaN(acc.x + acc.y + acc.z)) {
            continue;
        }
        count++;
        averageAccValues.x += acc.x;
        averageAccValues.y += acc.y;
        averageAccValues.z += acc.z;
    }
    averageAccValues.x /= count;
    averageAccValues.y /= count;
    averageAccValues.z /= count;

    if (client.readyState !== client.CLOSED) {
        client.send(["acc", 0, averageAccValues.x, averageAccValues.y, averageAccValues.z].join(","));
    }
    // console.log((new Date()).toFormat('YYYYMMDDHH24MISS'));
    console.log(averageAccValues.x.toFixed(3), averageAccValues.y.toFixed(3), averageAccValues.z.toFixed(3));
    // oscClient.send("/acc", [0, averageAccValues.x, averageAccValues.y, averageAccValues.z].join(","))
});
