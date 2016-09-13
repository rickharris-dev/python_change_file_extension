#!/usr/bin/python
from sys import argv
from os import listdir, rename
from re import compile, match

def rename_extension(path, extension, new_extension):
	expression = compile('.*\.' + extension + '$')
	files = [file for file in listdir(path) if expression.match(file)]

	# Check if path has / at the end
	if not compile('.*/$').match(path):
		path = path + '/'
		
	# Update files
	if len(files) == 0:
		print 'No files to update'
	else:
		for file in files:
			try:
				old_name = path + file
				new_name = path + file[:-3:] + new_extension
				rename(old_name, new_name)
				print 'Updated ' + new_name
			except:
				print 'Error: Could not rename ' + old_name

if __name__ == '__main__':
	path = argv[1]
	extension = argv[2]
	new_extension = argv[3]
	rename_extension(path, extension, new_extension)
