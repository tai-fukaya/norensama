/**
 * 人感センサーを取得する
 * 人が通ったら、一定期間、LEDを光らせる
 */
require('date-utils');
const Obniz = require('obniz');

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
                console.log(pos + "," + now.toFormat('YYYYMMDDHH24MISS'));
                if (timer) {
                    clearTimeout(timer);
                    timer = null;
                } else {
                    motionSensorStatuses[pos] = "MOVING";
                    mo0.display.clear();
                    for (let i in motionSensorStatuses) {
                        mo0.display.print(i + "" + motionSensorStatuses[i]);
                    }
                }
                timer = setTimeout(() => {
                    console.log("stop");
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
