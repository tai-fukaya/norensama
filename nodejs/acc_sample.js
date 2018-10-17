const Obniz = require('obniz');

let acc0 = new Obniz("6364-1751");
let accValueArray = [];

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

    console.log(averageAccValues.x.toFixed(3), averageAccValues.y.toFixed(3), averageAccValues.z.toFixed(3));
    
});

acc0.onconnect = async function() {

}

acc0.onclose = async function() {

}
