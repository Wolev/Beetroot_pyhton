# WEEK2
# Task4: Make the program check if the answer is correct and print it

'''
What do you want?
pass the computer the expresion from string to int
if it's int, make the input request
compare the int value with the input
if wrong, state the correct value
do it forever until you press exit
'''

while True:
	
  print("Type exit to exit the program.")
  expression = input("Input the mathematical expression: ")

  if expression == "exit":
    answer = input("If you want to exit type yes else type no: ")
    if answer == 'yes':
      break
    else:
      continue

  try:
    eval(expression)
  except:
	  print("Type a correct mathematical expression, not a string. ")
	  continue

  answer = int(input("Input the numerical answer: "))

  if eval(expression) == answer:
	  print(f"The answer to {str(expression)} is {str(answer)}. Correct!")
  else:
    print(f"No, the correct answer is {eval(expression)}.")
