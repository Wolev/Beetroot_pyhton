# WEEK3 HOMEWORK2
# Lesson: Dictionaries, for loops, comprehensions

# Task1: Make a program that has a string input
# and returns a dict containing every letter

"""
Action plan:
* Declare a variable that inputs a string
* Declare an empty dictionary
* Make a loop that assigns to every key a string letter
"""

# Declare input string variable
string_variable = input("Input a string variable: ")

# Declare empty dictionary
dictionary_string = dict()

# Create the loop
for i in range(len(string_variable)):
	dictionary_string[i] = string_variable[i]

# Print the dictionary
print(dictionary_string)

