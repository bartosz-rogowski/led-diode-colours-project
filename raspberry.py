# !/usr/bin/env/python3

import serial
from sys import exit
import time
import colorsys
from the_vault \
	import get_average_colour_from_screen, print_menu, clear_console

if __name__ == '__main__':
	
	# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	# ser.reset_input_buffer()
	# switch = ['1', '2']
	while True:
		try:
			clear_console()
			print_menu()
			choice = int(input('Enter your choice: '))
			# if ser.in_waiting > 0:
				# line = ser.readline().decode('utf-8').rstrip()
				# print(line)
			#for char in switch:
				#ser.write(char.encode())
				#line = ser.readline().decode('utf-8').rstrip()
				#print(line)
				# time.sleep(1)
			if choice == 0:
				exit(0)
			if choice == 1:
				clear_console()
				print("AVERAGE SCREEN COLOUR MODE")
				while True:
					try:
						colours = get_average_colour_from_screen()
						print(colours)
					except KeyboardInterrupt:
						break


			if choice == 2:
				clear_console()
				print("LIGHT SENSOR MODE")
				while True:
					try:
						print("Blank Space (for now)")
						time.sleep(10)
					except KeyboardInterrupt:
						break


			if choice == 3:
				clear_console()
				print("RAINBOW MODE")
				while True:
					try:
						print("Blank Space (for now)")
						time.sleep(10)
					except KeyboardInterrupt:
						break
	
	
		except KeyboardInterrupt:
			print("\nStopped by user")
			exit(0)
		except Exception:
			pass
