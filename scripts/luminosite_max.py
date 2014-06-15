# -*- coding: utf-8 -*-
# Python 2

import os
import json
import numpy
import cv2
import mycv

def process(imPath, jsonPath):
  im = mycv.loadImg(imPath)
  with open(jsonPath, 'r') as f:
	  jsonData = json.loads(f.read())

  ciel = {
    "date": "2014-06-15",
    "luminosite_max": int(numpy.ndarray.max(im))
  }
  
  jsonData["images"]["ciel"] = ciel
  with open(jsonPath, 'w') as outfile:
    json.dump(jsonData, outfile, indent = 2)

def main():
	for dirname, dirnames, filenames in os.walk('../analyse/sol/nuit/canal_rouge'):
	  if "ciel.png" in filenames and "details.json" in filenames:
	    imPath = os.path.join(dirname, "ciel.png")
	    jsonPath = os.path.join(dirname, "details.json")
	    process(imPath, jsonPath)

if __name__ == '__main__':
  main()
