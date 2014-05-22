# -*- coding: utf-8 -*-
# Python 2
# GIMP required

import os
import sys

# Path from gimpfu.gimp.__file__ in GIMP's Python-Fu console
sys.path.append("/usr/lib/gimp/2.0/python")

import gimpfu

SIZE = 800
allowedExts = ['jpg', 'jpeg', 'png']

def parsePath(path):
	name, ext = os.path.splitext(path)
	ext = ext[1:].lower() # Remove "."
	
	return name, ext


def checkPath(path):
	if not(os.path.isfile(path)):
		return False
		
	name, ext = parsePath(path)
	
	return (ext in allowedExts)


def createIm(path):
	name, ext = parsePath(path)
	
	if ext == 'jpg' or ext == 'jpeg':
		return gimpfu.gimp.pdb.file_jpeg_load(path, path)
	elif ext == 'png':
		return gimpfu.gimp.pdb.file_png_load(path, path)


def getImDims(im, size):
	width = gimpfu.gimp.pdb.gimp_image_width(im)
	height = gimpfu.gimp.pdb.gimp_image_height(im)
	m = max(width, height)
	
	if m <= size:
		return width, height
	else:
		factor = float(m)/size
		return (float(width)/factor), (float(height)/factor)
	

def main(paths):
	for path in paths:
		# Check files
		if not(checkPath(path)):
			print 'Error with {}'.format(path) 
			return
		
		filename, ext = parsePath(path)
		filename = filename.split('/')
		filename = filename[len(filename) - 1]
		
		savePath = 'resultats/' + filename
		
		# Create image
		# im = createIm(path)
		
		# Resize it
		# width, height = getImDims(im, SIZE)
		# gimpfu.gimp.pdb.gimp_image_scale(im, width, height)
		
		print savePath
		
		# Save it
		# gimpfu.gimp.pdb.file_jpeg_save(im, gimpfu.gimp.pdb.gimp_image_active_drawable(im), filename, filename, 0.8)		
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1:])
	else:
		print 'No image to be processed.'
