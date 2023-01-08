# WEEK2
# Task3: From an input string create 5 other random strings

import random

input_string = str(input("Input the desired string:"))
print("The input string inputed is {}".format(input_string))

list_of_strings = []

for r in range(5):
	result_string = ''.join(random.choice(input_string) for i in range(5))
	list_of_strings.append(result_string)

# Print the results

# Why does this not work?
# print("The random strings resulted from the inputs are " *list_of_strings, sep=',')

# This works so that's great.
print(*list_of_strings, sep=',')

