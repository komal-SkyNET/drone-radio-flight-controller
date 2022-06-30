#!/usr/bin/env python
import time
import serial

ser = serial.Serial('/dev/ttyS0', baudrate=100000,
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_TWO)

counter=0

while 1:
        ser.write(counter)
        time.sleep(1)
        counter += 1
