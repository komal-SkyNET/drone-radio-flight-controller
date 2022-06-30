#!/usr/bin/env python
import time
import serial

ser = serial.Serial('/dev/ttyS0', baudrate=100000,
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_TWO)
while 1:
        x=ser.readline()
        print(x)
