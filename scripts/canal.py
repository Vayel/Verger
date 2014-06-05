# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import os
import sys
import re
import numpy
import cv2
import mycv
from functions import *
from consts import *

RED_CHANNEL = 2
GREEN_CHANNEL = 1
BLUE_CHANNEL = 0
CHANNELS_LABELS = {
  'r': RED_CHANNEL,
  'g': GREEN_CHANNEL,
  'b': BLUE_CHANNEL
}


def printUsage():
  print """USAGE:
  Python 2 required
  OpenCV required
  python canal.py 
    --from path/folder/ 
    --to path/folder/ 
    --channel r|g|b
  Ex: python canal.py --from ../acquisition/sol/nuit/img/judor/ --to ../analyse/sol/nuit/canal_rouge/ --channel r
  """
  

def parseArgs(args):
  data = parseArgsToFrom(args)
  data["channel"] = None
  
  for i in range(len(args)):
    try:
      if args[i] == "--channel":
        val = args[i+1].lower()
        data['channel'] = CHANNELS_LABELS[val]
        i += 1
    except:
      pass
      
  if not(data["channel"]) or not(data["to"]) or not(data["from"]):
    printUsage()
    sys.exit()
             
  return data


def process(path, data):
  """
    Load "path" before getting its "requiredChannel" channel and
    saving it.
  """
  img = mycv.loadImg(path)
  channel = numpy.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
  channel[:,:] = img[:,:,data["channel"]]
  
  variety, source = parseImgPath(path)
  channelLetter = [k for k, v in CHANNELS_LABELS.iteritems() if v == data["channel"]][0]
  
  dirPath = '{}{}/{}/'.format(data["to"], variety, source)
  ensureDir(dirPath)
  imgPath = '{}can{}.jpg'.format(dirPath, channelLetter)
  cv2.imwrite(imgPath, channel)
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
  else:
    printUsage()
