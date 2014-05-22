# -*- coding: utf-8 -*-
# Python 2
# GIMP required

import os
import sys

# Path from gimp.__file__ in GIMP's Python-Fu console
sys.path.append("/usr/lib/gimp/2.0/python")

import gimpfu

allowedExts = ['jpg', 'jpeg', 'png']

def main(args):
	pass

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1:])
	else:
		print 'No image to be processed.'
