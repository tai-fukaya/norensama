#include<Wire.h>
const int MPU_addr=0x68;  // I2C address of the MPU-6050
float AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
int first_check = 1;             //自分の名前の送信処理が終了すると0になる
String get_data;                 //シリアルで受け取るデータの保管場所
String Get_tell = "Tell_Me_Your_Name";  //pythonから送信される文字列  
String check_OK = "ok";
String MyName = "GY-521";         //自分の名前の定義
int SerialSpeed = 9600;                 //シリアル通信のスピードを設定

void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
    Serial.begin(SerialSpeed);         
     
    //Get_tellと同じ文字列が入力されたら名前を送信しfirst_check=0にする
    //first_checkが1である限り以下の処理を続ける。
    while(first_check == 1){                     
        //シリアルから入力があるかチェックする
        if(Serial.available()){       
            //シリアルからの入力をget_dataに保管(#で始めと終わりを定義)
            //python側では'#Tell_Me_Your_Name#'と送信
            get_data = Serial.readStringUntil('#');  
                
            //入力された文字列がGet_tellと同じなら以下の処理実行                                      
            if(get_data == Get_tell){           
                Serial.print(MyName);     //自分の名前を送信
               digitalWrite(13, LOW);      //送信完了したらLEDをoffにする
            }           
            if(get_data == check_OK){          
                 //入力された文字列がcheck_OKと同じなら
                 //whileから抜けるためfirst_checkを0にする
                first_check = 0;                
            }            
        }    
    } 
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
}
void loop(){
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
  //Serial.print("AcX = "); 
  if(Serial.available()){       
      get_data = Serial.readStringUntil('#');
          if(get_data == check_OK){          
              Serial.print(AcX);Serial.print("\n"); 
              Serial.print(AcY);Serial.print("\n"); 
              Serial.print(AcZ);Serial.print("\n"); 
              Serial.print(GyX);Serial.print("\n"); 
              Serial.print(GyY);Serial.print("\n"); 
              Serial.print(GyZ);Serial.print("\n"); 
           }
    }   
  //Serial.print(Tmp/340.00+36.53);  //equation for temperature in degrees C from datasheet
}
