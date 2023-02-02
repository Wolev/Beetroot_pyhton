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
	count_lines(file)
	count_chars(file)


test("book.txt")
