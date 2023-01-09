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

def make_operation(operator,*num):
	string = ""

	for n in num:
		string += f"{n}{operator}"

	final_string = string[:-1]	

	print(f"The {final_string} expression has the answer: ")
	print(eval(final_string))
		

make_operation('+', 7, 7, 2) #returns 16
make_operation('-', 5, 5, -10, -20) #returns 30
make_operation('*', 7, 6) #returns 42
		
