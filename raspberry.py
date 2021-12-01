# !/usr/bin/env/python3

import serial
from sys import exit
import time
import colorsys
from the_vault \
	import get_average_colour_from_screen, get_rainbow_colour, print_menu, clear_console

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
				# mode = 1
				# ser.write(mode.encode())
				while True:
					try:
						colours = get_average_colour_from_screen()
						print(colours)
						# message = f"{colours[0]},{colours[1]},{colours[2]}"
						# ser.write(message.encode())
					except KeyboardInterrupt:
						# flag = 1
						# message = f"0,0,0,{flag}"
						# ser.write(message.encode())
						break


			if choice == 2:
				clear_console()
				print("LIGHT SENSOR MODE")
				# mode = 1
				# ser.write(mode.encode())
				while True:
					try:
						print("Blank Space (for now)")
						time.sleep(10)
						# message = f"{colours[0]},{colours[1]},{colours[2]}"
						# ser.write(message.encode())
					except KeyboardInterrupt:
						# flag = 1
						# message = f"0,0,0,{flag}"
						# ser.write(message.encode())
						break


			if choice == 3:
				clear_console()
				print("RAINBOW MODE")
				# mode = 1
				# ser.write(mode.encode())
				while True:
					try:
						for hue in np.linspace(0, 1, 100):
							(r, g, b) = get_rainbow_colour(hue)
							# message = f"{colours[0]},{colours[1]},{colours[2]}"
							# ser.write(message.encode())
							time.sleep(10)
							# message = "0, 0, 0"
							# ser.write(message.encode())
					except KeyboardInterrupt:
						# flag = 1
						# message = f"0,0,0,{flag}"
						# ser.write(message.encode())
						break
	
	
		except KeyboardInterrupt:
			print("\nStopped by user")
			exit(0)
		except Exception:
			pass
