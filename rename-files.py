#!/usr/bin/python
from sys import argv
from os import listdir, path, rename
from re import compile, match

def rename_extension(file_path, extension, new_extension):
	try:
		# Check if path exists
		path.exists(file_path)

		# Check if is directory
		path.isdir(file_path)

		# Check if path has / at the end
		if not compile('.*/$').match(file_path):
			file_path = file_path + '/'

		# Check if extensions have . at the front
		extension_test = compile('^\..*')
		if extension_test.match(extension):
			extension = extension[1::]

		if extension_test.match(new_extension):
			new_extension = new_extension[1::]

		# Create regex and find matching files
		expression = compile('.*\.' + extension + '$')
		files = [file for file in listdir(file_path) if expression.match(file)]

		# Update file extensions
		if len(files) == 0:
			print 'No files to update'
		else:
			for file in files:
				try:
					# Rename each file
					length = len(extension) * -1
					old_name = file_path + file
					new_name = file_path + file[:length:] + new_extension
					rename(old_name, new_name)
					print 'Updated ' + new_name
				except:
					print 'Error: Could not rename ' + old_name
	except Exception as e:
		if 'Not a directory' in e:
			print "The path given is not a directory"
		else:
			print "File path does not exist"

if __name__ == '__main__':
	file_path = argv[1]
	extension = argv[2]
	new_extension = argv[3]
	rename_extension(file_path, extension, new_extension)
