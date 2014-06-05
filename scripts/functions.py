# -*- coding: utf-8 -*-
# Python 2

import os
import sys
import re


def parseArgsToFrom(args):
  data = {
    "to": None,
    'from': None
  }
  for i in range(len(args)):
    try:
      if args[i] == "--to":
        assert args[i+1][-1:] == '/' # End with "/"
        data['to'] = args[i+1]
        i += 1
          
      elif args[i] == "--from":
        assert args[i+1][-1:] == '/' # End with "/"
        data['from'] = args[i+1]
        i += 1
    except:
      pass
      
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
