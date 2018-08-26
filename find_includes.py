#!/usr/bin/env python

import os
import sys
import re

cpp_extensions = set(['cc', 'h', 'hpp', 'cpp'])

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

def check_filename(filename):
	filename_arr = filename.split('.')
	if(len(filename_arr) < 2):
		return False
	
	if filename_arr[1] not in cpp_extensions:
		return False

	return True

def build_map_includes(directory, prepend_path = ''):
	heierarchy = {}

	
	for(dirpath, dirnames, filenames) in os.walk(directory):
		for filename in filenames:
			if(check_filename(filename)):
				path = dirpath.split(directory)[1]
				heierarchy[path + filename]  = find_includes(dirpath + '/' +  filename)
			
	return heierarchy

if __name__ == '__main__':
	if(len(sys.argv) > 2):
		build_map_includes(sys.argv[1], sys.argv[2])
	else:
		build_map_includes(sys.argv[1])
