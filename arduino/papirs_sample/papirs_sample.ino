String get_data;                 //シリアルで受け取るデータの保管場所
String Get_tell = "Tell_Me_Your_Name";  //pythonから送信される文字列  
String check_OK = "ok";
String MyName = "Papirs-01";         //自分の名前の定義
int SerialSpeed = 9600;              //シリアル通信のスピードを設定

const int PIRpin = 2;
const int LEDpin = 13;

void setup()
{
  pinMode(LEDpin, OUTPUT);
  Serial.begin(SerialSpeed);

  while (true) {
    if (Serial.available()) {
      get_data = Serial.readStringUntil('#');
      if (get_data == Get_tell) {
        Serial.print(MyName);
      }
      if (get_data == check_OK) {
        break;
      }
    }
  }
}

void loop()
{
  if (Serial.available()) {
    get_data = Serial.readStringUntil('#');
    if (get_data == check_OK) {
       if (digitalRead(PIRpin) == HIGH) {
         digitalWrite(LEDpin, HIGH);
         Serial.print("1\n");
       } else {
         digitalWrite(LEDpin, LOW);
         Serial.print("0\n");
       }
    }
  }
}
