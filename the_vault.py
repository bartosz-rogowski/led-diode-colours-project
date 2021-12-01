'''
This module contains tools and algorithms helpful in project.
'''
import numpy as np
from PIL import ImageGrab
import time
import os
import colorsys

def print_menu():
    '''Function printing menu on terminal.
    '''
    print("\t\tMain Menu:\n")
    print("0 - Exit")
    print("1 - Set diode colour to average one from the screen")
    print("2 - Set diode colour to one detected with light sensor")
    print("3 - Set diode colour to RAINBOW MODE")
    print()
    print("-"*44)
    print("In order to exit from any mode, press Ctrl+C")
    print("-"*44)
    print()

def clear_console():
    '''Simple function clearing console (multiplatform version)
    '''
    os.system('cls' if os.name=='nt' else 'clear')

def most_frequent(List):
	counter = 0
	num = List[0] 
	  
	for i in List: 
		curr_frequency = List.count(i) 
		if(curr_frequency > counter): 
			counter = curr_frequency 
			num = i 
  
	return num 

def get_average_colour_from_screen(screen_size: tuple=(1920,1080), step: int=40):
	''' returns average value of (rbg) from screen

	Arguments:
		screen_size - pixel size of screen given in tuple (width, height)
		step - number of pixels 
			(calculating with small step would take a lot of time
			and big step will not be effective and truthful)
	'''
	num_pixel = screen_size[0]//step * screen_size[1]//step

	img = ImageGrab.grab()
	imgNP = np.array(img)

	im_arr = np.frombuffer(img.tobytes(), dtype=np.uint8)
	im_arr = im_arr.reshape((img.size[1], img.size[0], 3))
	r = g = b = 0
	pixel_array = []
	for y in range(0, screen_size[1], step):
		for x in range(0, screen_size[0], step):
			px = im_arr[y][x]

			pixel_array.append([px[0], px[1], px[2]])

	colour = most_frequent(pixel_array)
	return colour


def get_rainbow_colour(hue):
	(r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
	rainbow_colour = (int(255 * r), int(255 * g), int(255 * b))
	return rainbow_colour