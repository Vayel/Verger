# Python 2

import cv2

def loadImg(path):
	im = cv2.imread(path)
	if im == None:
		print "Error loading " + path
		import sys
		sys.exit()
	else:
		return im
