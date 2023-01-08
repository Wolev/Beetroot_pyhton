#Task1: String it

# declare the original string
original_string = input("Input the original string:")

# declare the final string
result_string = ''

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
