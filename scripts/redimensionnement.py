# -*- coding: utf-8 -*-
# Python 2
# GIMP required

import os
import sys

# Path from gimpfu.gimp.__file__ in GIMP's Python-Fu console
sys.path.append("/usr/lib/gimp/2.0/python/")

import gimpfu
"""
Ouvrir GIMP
Filtres > Python-Fu > Console
>>> import sys
>>> sys.path.append(chemin-du-script)
>>> import script
>>> script.work(...)
"""

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
	

def work(paths, saveFolder='./', size=800):
	for path in paths:
		# Check files
		if not(checkPath(path)):
			print 'Error with {}'.format(path) 
			return
		
		filename, ext = parsePath(path)
		filename = filename.split('/')
		filename = filename[len(filename) - 1]
		
		savePath = saveFolder + filename + '.' + ext
		
		# Create image
		im = createIm(path)
		
		# Resize it
		width, height = getImDims(im, size)
		gimpfu.gimp.pdb.gimp_image_scale(im, width, height)
		
		# Save it
		gimpfu.gimp.pdb.file_jpeg_save(im, gimpfu.gimp.pdb.gimp_image_active_drawable(im), savePath, savePath, 0.9, 0, 0, 0, "", 0, 0, 0, 0)
