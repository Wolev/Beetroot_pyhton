# WEEK3 HOMEWORK1
# Lesson: List, tuples, sets

# Task2: make 2 lists with random integers
# Make a third list that contains the common values of the 2 lists

"""
Action plan:
* generate two lists with the random module
* need to go through the list to compare:
	  ** i for the first list
		** is list1[i] in list2
		** if true, list3.append(list1[i])
		** what's the lenght? don't matter which list you pick
"""

import random as rd

# Generate two lists
list1 = [rd.randint(0,20) for _ in range(10)]
list2 = [rd.randint(0,20) for _ in range(10)]

# Generate the empty common list
list3 = []

# Generate for loop to go through the list1
for i in range(len(list1)):
	# Take the duplicate case first
	if list1[i] in list3:
		pass
	# Use append when you find values
	elif list1[i] in list2:
		list3.append(list1[i])

print(f"List the 1st list here: {list1}")
print(f"List the 2nd list here: {list2}")
print(f"List of the common values: {list3}")
