# -*- coding: utf-8 -*-

import sys
# Path from gimp.__file__ in GIMP's Python-Fu console
sys.path.append("/usr/lib/gimp/2.0/python")
import gimp

def main():
	help(gimp)
	
if __name__ == '__main__':
	main()
