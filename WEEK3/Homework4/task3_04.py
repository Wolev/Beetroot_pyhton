# WEEK3 HOMEWORK2
# Lesson: A simple calculator

# Task3: Simple calculator

"""
Action plan:

* define the make_operation function
* use args for all the arguments that are not the operator
* create an empty string
* concatenate the arguments
* remove the final character from the string
* use the eval function to initialise the string expression 
"""

def make_operation(operator, *numbers):
	numbers_int_converted = list()
	difference = 0
	for number in numbers:
		numbers_int_converted.append(int(number))
	
	if operator == "+":
		# return sum(numbers_int_converted)
		result = sum(numbers_int_converted)

		# For args you don't need to use the * in the function when printing
		# You need to use *args when iterating in the function

		# print(f"The values to be added are: {numbers}")

		print(f"The values to be added are: {numbers_int_converted}")
		print(f"The result of the sum is: {result}\n")

	elif operator == "-":
		# return numbers_int_converted[0] - sum(numbers_int_converted[1:])
		# print(numbers_int_converted[0] - sum(numbers_int_converted[1:]))A

		result = numbers_int_converted[0] - sum(numbers_int_converted[1:])
		print(f"The values to be substacted are: {numbers_int_converted}")
		print(f"The result of the substraction is: {result}\n")

	elif operator == "*":
		multiply_result = 1
		for number in numbers_int_converted:
			multiply_result *= number
		# return multiply_result
		print(f"The values to be multiplied are: {numbers_int_converted}")
		print(f"The result of the multiplication is: {multiply_result}\n")

make_operation('+', 7, 7, 2) #returns 16
make_operation('-', 5, 5, -10, -20) #returns 30
make_operation('*', 7, 6) #returns 42
		
