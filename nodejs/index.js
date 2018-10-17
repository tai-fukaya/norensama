/**
 * 人感センサーを取得する
 * 人が通ったら、一定期間、LEDを光らせる
 */
require('date-utils');
const osc = require('node-osc');
const Obniz = require('obniz');

let oscClient = osc.Client('127.0.0.1', 57120);

// motion-sensor
let mo0 = new Obniz("8894-3916");
mo0.onconnect = async function () {
    console.log("connect", mo0.id);
    mo0.display.clear();
    mo0.display.print("hello");
    let motionSensorStatuses = ["", ""];
    let onMotionSensorChange = (p) => {
        let pos = p;
        let timer = null;
        return (val) => {
            if (val) {
                let now = new Date();
                // console.log(pos + "," + now.toFormat('YYYYMMDDHH24MISS'));
                if (timer) {
                    clearTimeout(timer);
                    timer = null;
                } else {
                    console.log("start", pos);
                    // oscClient.send("/motion", [0, pos, "start"].join(","));
                    motionSensorStatuses[pos] = "MOVING";
                    mo0.display.clear();
                    for (let i in motionSensorStatuses) {
                        mo0.display.print(i + "" + motionSensorStatuses[i]);
                    }
                }
                timer = setTimeout(() => {
                    console.log("stop", pos);
                    // oscClient.send("/motion", [0, pos, "stop"].join(","));
                    motionSensorStatuses[pos] = "";
                    mo0.display.clear();
                    for (let i in motionSensorStatuses) {
                        mo0.display.print(i + "" + motionSensorStatuses[i]);
                    }
                    timer = null;
                }, 2000);
            }
        }
    };

    let motionSensor0 = mo0.wired("PaPIRsVZ", {
        gnd:0, signal:1, vcc:2
    });
    motionSensor0.onchange = onMotionSensorChange(0);

    let motionSensor1 = mo0.wired("PaPIRsVZ", {
        gnd:4, signal:5, vcc:6
    });
    motionSensor1.onchange = onMotionSensorChange(1);
}

mo0.onclose = async function() {
    console.log("close");
    // あんまりつかえないかも？
}

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

    // console.log(averageAccValues.x.toFixed(3), averageAccValues.y.toFixed(3), averageAccValues.z.toFixed(3));
    // oscClient.send("/acc", [0, averageAccValues.x, averageAccValues.y, averageAccValues.z].join(","))
});
