#!/usr/bin/env/python3

import serial
import sys
import time
import colorsys

if __name__ == '__main__':
    
    (r, g, b) = colorsys.hsv_to_rgb(1.0, 1.0, 1.0)
    
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    switch = ['1', '2']
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            #for char in switch:
                #ser.write(char.encode())
                #line = ser.readline().decode('utf-8').rstrip()
                #print(line)
                #time.sleep(1)
        
        except KeyboardInterrupt:
            print("Zamykamy")
            sys.exit(0)
