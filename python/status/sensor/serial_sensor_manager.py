#-*-coding:utf-8-*-
import serial
import commands
import time


class SerialSensorManager(object):

    def __init__(self):
        self._sensors = {}
    
    def search(self, keys):
        # for Mac
        usb_list = commands.getoutput('ls /dev | grep tty.usbmodem*').split('\n')
        print(usb_list)
        # Open port
        serial_list = [serial.Serial("/dev/%s"%usb) for _, usb in enumerate(usb_list)]
        time.sleep(2.)
        # Ask name
        for i, ser in enumerate(serial_list):
            ser.write("#Tell_Me_Your_Name#")
        time.sleep(2.)
        
        self._sensors = {}
        for i, ser in enumerate(serial_list):
            opt = commands.getoutput("cat /dev/%s"%usb_list[i])
            print(opt)
            self._sensors[opt] = ser
            ser.write("#ok#")

    def get_data(self, key):
        obj = self._sensors.get(key)
        if obj is None:
            return []
        obj.write("#ok#")
        data = commands.getoutput("cat %s" %obj.port).split("\n")
        return data
