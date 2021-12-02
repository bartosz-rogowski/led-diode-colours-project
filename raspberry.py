#!/usr/bin/env python3

import serial
import time
from sys import exit
import numpy as np
import time
from the_vault \
	import get_average_colour_from_screen, get_rainbow_colour, print_menu, clear_console

if __name__ == '__main__':
	
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	ser.reset_input_buffer()
	# switch = ['1', '2']
	while True:
		try:
			clear_console()
			print_menu()
			#time.sleep(1)
			choice = int(input('Enter your choice: '))
			if choice == 0:
				exit(0)
			if choice == 1:
				clear_console()
				print("AVERAGE SCREEN COLOUR MODE")
				mode = '1'
				ser.write(mode.encode())
				while True:
					try:
						(r, g, b) = get_average_colour_from_screen()
						#print(colours)
						message = "{r},{g},{b}\n".format(r = r, g = g, b = b)
						ser.write(message.encode())
					except KeyboardInterrupt:
						flag = 1
						message = "0,0,0,{flag}\n".format(flag = flag)
						ser.write(message.encode())
						break


			if choice == 2:
				clear_console()
				print("LIGHT SENSOR MODE")
				mode = '2'
				ser.write(mode.encode())
				while True:
					try:
						message = "0,\n"
						ser.write(message.encode())
						if ser.in_waiting > 0:
							line = ser.readline().decode('utf-8').rstrip()
							print(line)
					except KeyboardInterrupt:
						flag = 1
						message = "0,0,0,{flag}\n".format(flag = flag)
						ser.write(message.encode())
						break


			if choice == 3:
				clear_console()
				print("RAINBOW MODE")
				mode = '1'
				ser.write(mode.encode())
				
				while True:
					try:
						message = "255,255,255\n"
						ser.write(message.encode())
						time.sleep(1)

##                                    for hue in np.linspace(0, 1, 100):
##                                        print("everfore")
##                                        (r, g, b) = get_rainbow_colour(hue)
##                                        message = "{r},{g},{b}\n".format(r = r, g = g, b = b)
##                                        ser.write(message.encode())
##                                        print(r, g, b)
##                                        time.sleep(0.5)
										#message = "0,0,0\n"
										#ser.write(message.encode())
					except KeyboardInterrupt:
						flag = 1
						message = "0,0,0,{flag}\n".format(flag = flag)
						ser.write(message.encode())
						break
	
	
		except KeyboardInterrupt:
			print("\nStopped by user")
			exit(0)
		except Exception:
			pass