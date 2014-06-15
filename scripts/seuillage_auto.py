# -*- coding: utf-8 -*-
# Python 2

import os
import json
import time
import numpy
import cv2
import mycv
from functions import *

def updateJson(path, data, thresh, outImFilename):
  date = time.strftime("%Y-%m-%d", time.gmtime())
  filename, ext = splitPath(outImFilename)

  data["images"][filename] = {}
  data["images"][filename]["date"] = date
  data["images"][filename]["operations"] = ["can r", "seuil " + str(thresh)]
  
  with open(path, 'w') as outfile:
    json.dump(data, outfile, indent = 2)

def getSkyMaxLum(data):
  return data["images"]["ciel"]["luminosite_max"]

def getThreshDiff(path, data, lum):
  hand = int(data["images"]["canr_seuil"]["operations"][1][6:])
  return ("hand - lum = " + str(hand) + " - " + str(lum) + " = " + str(hand - lum))

def main(path):
  files = os.listdir(path)
  srcImFilename = "canr.jpg"
  jsonFilename = "details.json"
  outImFilename = "canr_seuil_auto.jpg"
  
  if not(jsonFilename in files):
    print "Error: " + jsonFilename + " not found."
    return
  
  with open(os.path.join(path, jsonFilename), 'r') as f:
	  jsonData = json.loads(f.read())
    
  try:
    skyMaxLum = getSkyMaxLum(jsonData)
  except KeyError:
    print "Error: " + jsonFilename + " does not have ['images']['ciel']['luminosite_max'] key."
    return
  
  if not(srcImFilename in files):
    print "Error: " + srcImFilename + " not found."
    return
      
  src = mycv.loadImg(os.path.join(path, srcImFilename))
  retval, thresholded = cv2.threshold(src, skyMaxLum, 255, cv2.THRESH_BINARY)
  
  cv2.imwrite(os.path.join(path, outImFilename), thresholded)
  updateJson(os.path.join(path, jsonFilename), jsonData, skyMaxLum, outImFilename)
  
  print path
  print getThreshDiff(path, jsonData, skyMaxLum)
  print ""
  
if __name__ == '__main__':
  for dirname, dirnames, filenames in os.walk('../analyse/sol/nuit/canal_rouge'):
    if "ciel.png" in filenames and "details.json" in filenames:
      main(dirname)
