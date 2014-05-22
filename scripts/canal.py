# -*- coding: utf-8 -*-
# Python 2
# GIMP required

import os
import sys

# Path from gimp.__file__ in GIMP's Python-Fu console
sys.path.append("/usr/lib/gimp/2.0/python")

import gimpfu

allowedExts = ['jpg', 'jpeg', 'png']

RED_CHANNEL = 0
GREEN_CHANNEL = 1
BLUE_CHANNEL = 2
channel = RED_CHANNEL 

def getChannel(args):
	pass
	# Find "--channel" in args
	# Default: red

def main(args):
	pass

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1:])
	else:
		print 'No image to be processed.'
