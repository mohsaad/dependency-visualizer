#!/usr/bin/env python

import os
import sys

def find_includes(filename):
	files = []

	f = open(filename, 'r')
	for line in f:
		sp = line.split('\n')[0].split('#include')
		if(len(sp) <= 1):
			continue
		
		included_file = sp[1].strip(' ').strip("<").strip(">").strip('"')
	
		files.append(included_file)
	
	f.close()
	return files


def build_map_includes(directory):
	files = os.listdir(directory)
	heierarchy = {}
	for name in files:
		heierarchy[name] = find_includes(name)

	print(heierarchy)

if __name__ == '__main__':
	print build_map_includes(sys.argv[1])
