import java.util.Date;
import oscP5.*;
import netP5.*;

OscP5 osc;
GraphList[] lists;
boolean[][] motionSensorStatus = {
  {false, false, false},
  {false, false, false}
};

void setup() {
  size(600, 600);
  frameRate(60);
  
  osc = new OscP5(this, 12000);
  lists = new GraphList[3];
  lists[0] = new GraphList("acc_x", color(0, 200, 200));
  lists[1] = new GraphList("acc_y", color(200, 200, 0));
  lists[2] = new GraphList("acc_z", color(200, 0, 200));
}

void draw() {
   background(0);
   
   translate(10, -10);
   stroke(255);
   for (boolean[] sensor : motionSensorStatus) {
     translate(0, 20);
     for (int i = 0; i < sensor.length; i++) {
       if (sensor[i]) {
         fill(255);
       } else {
         noFill();
       }
       rect(15*i, 0, 10, 10);
     }
   }

   translate(0, 30);
   long now = (new Date()).getTime();
   drawGraph(width - 20, 300, now, 4000.0, -1.5, 1.5, lists);
}

void oscEvent(OscMessage msg) {
  if (msg.checkAddrPattern("/acc") == true) {
    long now = (new Date()).getTime();
    lists[0].addData(now, msg.get(0).floatValue());
    lists[1].addData(now, msg.get(1).floatValue());
    lists[2].addData(now, msg.get(2).floatValue());
  } else if (msg.checkAddrPattern("/motion") == true) {
    int sensorId = msg.get(0).intValue();
    int motionId = int(msg.get(1).stringValue());
    String statusStr = msg.get(2).stringValue();
    boolean status = statusStr.equals("start");

    motionSensorStatus[sensorId][motionId] = status;
  }
}
