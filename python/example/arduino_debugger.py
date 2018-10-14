#-*-coding:utf-8-*-
# http://airoboticsandsoon.hatenablog.jp/entry/2017/12/03/214140

import commands
import time

import Connect_Start_Arduino

ArdName={"GY-521":None, "Papirs-01":None}
ArdName=Connect_Start_Arduino.UsbStart(ArdName)

def plot_data():
    ArdName["GY-521"].write("#ok#")
    data1 = commands.getoutput("cat %s" %ArdName["GY-521"].port).split("\n")
    ArdName["Papirs-01"].write("#ok#")
    data2 = commands.getoutput("cat %s" %ArdName["Papirs-01"].port).split("\n")
    print(data2)
    # if len(data1) != 6:
    #     return
    print(data1)

while True:
    plot_data()
    time.sleep(.1)
