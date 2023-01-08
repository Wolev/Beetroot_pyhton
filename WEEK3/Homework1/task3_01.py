# WEEK3 HOMEWORK1
# Lesson: List, tuple, set

# Task3:
# Make a list that contains all integers from 1 to 100
# Find all integers that are divisible by 7 and not multiple of 5
# Put those numbers in the list

"""
Action plan:
* Generate 1 list with all from 1 to 100 and 1 empty list.
* Check the requirements for the integer
* Append if correct
* Print final list
"""

print("Print the list that contains the numbers divisible by 7 and not multiple by 5. \n")

# Generate empty list
list_of100 = [ i for i in range(1,101)]
list_final = list()
list_courious = list()

# Declare empty iterable variable
number = 1

# Generate while loop
while number <= len(list_of100):
	if number % 7 == 0 and number % 5 != 0:
		list_final.append(number)
	elif number % 7 == 0:
		list_courious.append(number)
	number += 1

print(f"The final list of numbers is: {list_final}")

# Bonus challenge:
print(f"The list that divides to 7 and 5 is: {list_courious}")
