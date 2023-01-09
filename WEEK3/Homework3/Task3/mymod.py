# Create a function that reads and input file 
# Counts the number of lines in a file

def count_lines(file):
	file_read = open(file, "r") # string input .txt file	
	lines = file_read.readlines()
	print(f"Number of lines: {len(lines)}")

def count_chars(file):
	file_read = open(file, "r")
	data_read = file_read.read()
	print(f"Number of characters: {len(data_read)}")

def test(file):
	pass
"""
test(name) function that calls both counting functions with a given input file­name. Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
"""

count_lines("book.txt")	
count_chars("book.txt")
