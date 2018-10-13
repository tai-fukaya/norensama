#-*-coding:utf-8-*-
#必要なライブラリ
import serial
import commands
from time import sleep

#arduinoの名前を辞書型で用意されたものを引数として受け取りreturnする
def UsbStart(ArdName):
    #arduinoが最大100個繋がれたことを考慮して100この成分を含むリストを作成
    UsbSerial = [0 for i in range(100)]
    #arduinoはttyUSB0などと表示されるのでlinuxの
    #'ls /dev | grep ttyUSB*を実行しUSBinfoに格納
    USBinfo = commands.getoutput('ls /dev | grep tty.usbmodem*')
    #改行が\nとして入ってしまうので分割
    USBinfo = USBinfo.split('\n')

    print(USBinfo)
    #arduinoの接続数だけserial.Serialでポートを開放
    for i in range(len(USBinfo)):
        UsbSerial[i] = serial.Serial("/dev/%s" %USBinfo[i])

    sleep(2)     #これがないと上手くいかない

    #接続された全arduinoに'#Tell_Me_Your_Name#'と送信
    for i in range(len(USBinfo)):
        UsbSerial[i].write('#Tell_Me_Your_Name#')

    sleep(2)     #これがないと受信されないこと多かった

    #arduinoの名前とポートをリストで対応
    for i in range(len(USBinfo)):
        opt = commands.getoutput("cat /dev/%s" %USBinfo[i])
        print(opt)
        ArdName[opt]=UsbSerial[i]
        UsbSerial[i].write("#ok#")      #LOOPに移させる

    return ArdName

if __name__ == '__main__':
    UsbStart({"":None})
    