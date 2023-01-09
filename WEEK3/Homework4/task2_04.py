# WEEK3 HOMEWORK4
# Lesson: Functions 

# Task1: Make a function that makes a dicitionary

def make_country(name, capital):
	dictionary_country = dict(zip(name, capital))
	print("The dictionary is: \n")
	print(dictionary_country)


name_list = list()
capital_list = list()

while True:
	
	name = input("Name of the country: ")
	capital = input("Capital of the country: ")

	name_list.append(name)
	capital_list.append(capital)
	
	exit_value = input("Are these all the countries you want included? (yes/no): ")

	if exit_value.lower() == 'yes':
		break
	else:
		continue

make_country(name_list, capital_list)

