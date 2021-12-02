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
	ser.reset_output_buffer()

	while True:
		ser.reset_input_buffer()
		try:
			clear_console()
			print_menu()
			choice = int(input('Enter your choice: '))

			if choice == 0:
				exit(0)
			if choice == 1:
				clear_console()
				print("AVERAGE SCREEN COLOUR MODE")
				mode = '1'
				ser.write(mode.encode())
				while True:
					ser.reset_input_buffer()
					try:
						(r, g, b) = get_average_colour_from_screen()
						message = "{r},{g},{b},0\n".format(r = r, g = g, b = b)
						ser.write(message.encode())
					except KeyboardInterrupt:
						message = "0,0,0,1\n"
						ser.write(message.encode())
						break


			if choice == 2:
				clear_console()
				print("LIGHT SENSOR MODE")
				mode = '2'
				ser.write(mode.encode())
				while True:
					ser.reset_input_buffer()
					try:
						message = "0,0,0,0\n"
						ser.write(message.encode())
						time.sleep(0.05)
					except KeyboardInterrupt:
						message = "0,0,0,1\n"
						ser.write(message.encode())
						break


			if choice == 3:
				clear_console()
				print("RAINBOW MODE")
				mode = '1'
				ser.write(mode.encode())
				
				while True:
					ser.reset_input_buffer()
					try:
						for hue in np.linspace(0, 1, 100):
							(r, g, b) = get_rainbow_colour(hue)
							message = "{r},{g},{b},0\n".format(r = r, g = g, b = b)
							ser.write(message.encode())
							time.sleep(0.1)
					except KeyboardInterrupt:
						message = "0,0,0,1\n"
						ser.write(message.encode())
						break
	
	
		except KeyboardInterrupt:
			print("\nStopped by user")
			exit(0)
		except Exception:
			pass