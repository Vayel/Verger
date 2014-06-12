# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import json
import os

def process(contents):
	data = json.loads(contents)
	print data["images"]["canr_seuil"]["operations"][1]

def main():
	for dirname, dirnames, filenames in os.walk('../analyse/sol/nuit/canal_rouge'):
		for filename in filenames:
			path = os.path.join(dirname, filename)
			name, ext = os.path.splitext(path)
			if ext == '.json':
				with open(path, 'r') as f:
					process(f.read())
	
if __name__ == "__main__":
	main()
