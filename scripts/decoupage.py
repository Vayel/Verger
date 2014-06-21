# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import os
import sys
import random
import numpy
import cv2
import mycv
from functions import *


def printUsage():
  print """USAGE:
  Python 2 required
  OpenCV required
  python decoupage.py folder1 folder2
  """

def process(name, ext):
  variety, source = parseImgPath(name)
  img = mycv.loadImg(name + ext)
  height, width, channels = img.shape
  left_width = random.randint(0, width)
  right_width = width - left_width + 50
  left_img = img[:, :left_width, :]
  right_img = img[:, width - right_width:, :]
  
  save(variety, source, 'left' + ext, left_img)
  save(variety, source, 'right' + ext, right_img)
  path = '../cartographie/image_stitching/img/' + variety + '/' + source + '/'
  print 'Stitching ' + path + '...'
  os.system('../cartographie/image_stitching/bin/stitching ' + path + 'left' + ext + ' ' + path + 'right' + ext + ' --output ' + path + 'stitched.jpg')

def save(folder, num, filename, img):
  root = '../cartographie/image_stitching/img/'
  path = root + folder + '/'
  ensureDir(path)
  path += num + '/'
  ensureDir(path)
  path += filename
  cv2.imwrite(path, img)
  
def main(folders):
  for folder in folders:
    for dirname, dirnames, filenames in os.walk(folder):
      for filename in filenames:
        path = os.path.join(dirname, filename)
        name, ext = os.path.splitext(path)
        if ext == '.jpg' or ext == '.png':
          process(name, ext) 
  cv2.waitKey()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1:])
    cv2.destroyAllWindows()
  else:
    printUsage()
