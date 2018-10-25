const Obniz = require('obniz');
const osc = require('node-osc');

let oscClient = new osc.Client("127.0.0.1", 12000);

let acc0 = new Obniz("6364-1751");

acc0.onconnect = async () => {
    console.log('connect');
    let sensor = acc0.wired("KXR94-2050", {vcc:0, gnd:1, x:2, y:3, z:4 });
    sensor.onChange = values => {
        // 0.7 ~ -1.4
        // let x = convert(values.x, -1.5, 0.75, -0.98, 0.98);
        // let y = convert(values.y, -1.5, 0.75, -0.98, 0.98);
        // let z = convert(values.z, -0.98, 0.6, -0.98, 0.98);
        let x = values.x;
        let y = values.y;
        let z = values.z;

        console.log(`${x.toFixed(3)},${y.toFixed(3)},${z.toFixed(3)}`);
        let message = new osc.Message("/acc");
        message.append(x);
        message.append(y);
        message.append(z);
        oscClient.send(message);
    };
}

acc0.onclose = async () => {

}

function convert(v, bmi, bmx, ami, amx) {
    v = Math.min(bmx, v);
    v = Math.max(bmi, v);
    return ami + (v - bmi) * (amx - ami)/(bmx - bmi);
}
