#Task1: String it

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
# Declare the original string.

original_string = input("Input the original string:")

# declare the final string
result_string = ""

# declare the iterator
iterator = 0

# better way

while iterator <= len(original_string):
	if len(original_string) == 1:
		print("Empty String")
		break
	if len(original_string) == 2:
		print(original_string * 2)
		break
	elif iterator == len(original_string):
		result_string = original_string[0:2] + original_string[-2:]
		print(result_string)
	iterator += 1

# old way that is too long

"""
# declare the iterator
i = 0

while i <= len(original_string):
	if len(original_string) == 1:
		print("Empty String")
		break
	if len(original_string) == 2:
		print(original_string*2)
		break
	if i == 0:
		result_string += original_string[i]
	if i == 1:
		result_string += original_string[i]
	elif i == len(original_string)-2:
		result_string += original_string[i]
	elif i == len(original_string)-1:
		result_string += original_string[i]
	elif i == len(original_string):
		print(result_string)
	else:
		pass
	i+=1
"""

