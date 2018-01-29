#!/usr/bin/python

import serial	#Adds the serial library for python
import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('RGB LED Mimic')

s = serial.Serial("/dev/ttyACM0")	#Connects to the Arduino thru the serial port

while True:	#infinite loop
  l = s.readline()	#read a line from the Arduino thru serial
# l is currently formatted: "R,G,B"
# This is a string that our computer can't read
  colors = l.rstrip().split(",")	# turns the string into a list
  rgb = [int(color) for color in colors]

  DISPLAYSURF.fill(rgb)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()

