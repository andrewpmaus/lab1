#!/usr/bin/python

import serial	#Adds the serial library for python

s = serial.Serial("/dev/ttyACM0")	#Connects to the Arduino thru the serial port

while(True):	#infinite loop
  l = s.readline()	#read a line from the Arduino thru serial
# l is currently formatted: "R,G,B"
# This is a string that our computer can't read
  colors = l.rstrip().split(",")	# turns 
  rgb = [int(color) for color in colors]
  print rgb

