# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import os
import sys
import numpy
import cv2
import mycv
from functions import *
from consts import *


def printUsage():
  print """USAGE:
  Python 2 required
  OpenCV required
  python inversion.py 
    --from path/folder/ 
    --to path/folder/
  Ex: python inversion.py --from ../acquisition/sol/nuit/img/judor/ --to ../analyse/sol/nuit/inversion/
  """
  

def parseArgs(args):
  data = parseArgsToFrom(args)
      
  if not(data["to"]) or not(data["from"]):
    printUsage()
    sys.exit()
             
  return data


def process(path, data):
  """
    Load "path" before inverting the image and saving it.
  """
  img = mycv.loadImg(path)
  white = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=img.dtype)
  white[:,:,:] = [255, 255, 255]
  inv = cv2.subtract(white, img)
  
  variety, source = parseImgPath(path)
  dirPath = '{}{}/{}/'.format(data["to"], variety, source)
  ensureDir(dirPath)
  imgPath = '{}inv.jpg'.format(dirPath)
  cv2.imwrite(imgPath, inv)
  print '{} has been saved.'.format(imgPath)

  
def main(args):
  data = parseArgs(args)
  
  paths = getImgsPaths(data["from"])
  for path in paths:
    filename, ext = splitPath(path)
    if ext in ALLOWED_EXTS:
      process(path, data)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1:])
    cv2.destroyAllWindows()
  else:
    printUsage()
