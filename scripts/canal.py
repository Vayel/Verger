# -*- coding: utf-8 -*-
# Python 2
# GIMP required

import os
import sys
import re
import numpy
import cv2
import mycv

allowedExts = ['jpg', 'jpeg', 'png']

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
    --saveTo path/folder/ 
    --channel r|g|b
  Ex: python canal.py --from ../acquisition/sol/nuit/img/judor/ --saveTo ../analyse/sol/nuit/canal_rouge/ --channel r
  """
  

def parseArgs(args):
  data = {
    "channel": None,
    "saveTo": None,
    'from': None
  }
  err = False
  
  for i in range(len(args)):
    try:
      if args[i] == "--channel":
        val = args[i+1].lower()
        data['channel'] = CHANNELS_LABELS[val]
        i += 1
          
      elif args[i] == "--saveTo":
        assert args[i+1][-1:] == '/' # End with "/"
        data['saveTo'] = args[i+1]
        i += 1
          
      elif args[i] == "--from":
        assert args[i+1][-1:] == '/' # End with "/"
        data['from'] = args[i+1]
        i += 1
    except:
      pass
      
  if not(data["channel"]) or not(data["saveTo"]) or not(data["from"]):
    printUsage()
    sys.exit()
             
  return data


def getImgsPaths(folder):
  return [folder + filename for root, dirs, files in os.walk(folder) for filename in files]


def splitPath(path):
  filename, ext = os.path.splitext(path)
  ext = ext[1:].lower() # Remove "."
  return filename, ext 


def parseImgPath(path):
  variety = 'defaultVariety'
  source = 'defaultSource'
  
  match = re.findall(r'acquisition/sol/nuit/img/(.+)/(.+)', path)
  try:
    variety = match[0][0]
    source, ext = splitPath(match[0][1])
  except:
    pass
  
  return variety, source


def ensureDir(path):
  d = os.path.dirname(path)
  if not(os.path.exists(d)):
    os.makedirs(d)

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
  
  dirPath = '{}{}/{}/'.format(data["saveTo"], variety, source)
  ensureDir(dirPath)
  imgPath = '{}can{}.jpg'.format(dirPath, channelLetter)
  cv2.imwrite(imgPath, channel)
  print '{} has been saved.'.format(imgPath)
  
def main(args):
  data = parseArgs(args)
  
  paths = getImgsPaths(data["from"])
  for path in paths:
    filename, ext = splitPath(path)
    if ext in allowedExts:
      process(path, data)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1:])
  else:
    print 'No image to be processed.'
