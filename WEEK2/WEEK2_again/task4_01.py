# WEEK2
# Task4: Make the program check if the answer is correct and print it

print("2 + 2 = ?")
answer = int(input("Give answer here:"))

if answer == (2+2):
	print("The answer is correct, 2+2=4.")
else:
	print("The answer is incorrect. The answer is {}.".format(str(2+2)))
