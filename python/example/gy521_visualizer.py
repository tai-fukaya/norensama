#-*-coding:utf-8-*-
# http://airoboticsandsoon.hatenablog.jp/entry/2017/12/03/214140

import commands
import time

import Connect_Start_Arduino

ArdName={"GY-521":None}
ArdName=Connect_Start_Arduino.UsbStart(ArdName)

def plot_data():
    ArdName["GY-521"].write("#ok#")
    data = commands.getoutput("cat %s" %ArdName["GY-521"].port).split("\n")
    if len(data) != 6:
        return
    print(data)

while True:
    plot_data()
    time.sleep(.1)
