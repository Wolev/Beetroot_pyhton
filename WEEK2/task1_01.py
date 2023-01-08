# WEEK2
# Task1: Guessing game
# Generate a random number 1-10 and guess it

import random

# Input the human guess
try:
	human_guess = int(input("Input a number between 1 and 10: "))
	if human_guess > 10 or human_guess < 0:
		human_guess = int(input("""Between 1 and 10 included. No greater or 
														smaller number allowed."""))
except:
	print("Type a number not a string!")

# Generate computer guess
computer_guess = random.randint(1,10)

# Prints the computer guess for debugging
# print(computer_guess)

# Check if the guess is right
if human_guess == computer_guess:
	print("Yes, the number is {}".format(human_guess))
else:
	print("No, you guessed wrong. The number is {}".format(computer_guess))
	print("You were of by {}.".format(abs(computer_guess-human_guess))) # Shows how close the guess was
