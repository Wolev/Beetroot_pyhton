#Task3: check if names are the same 

# Input the names
name1 = input("Input the first name:")
name2 = input("Input the second name:")

# Check their sameness
if name1.lower() == name2.lower():
	print("{0} and {1} are the same name and valid.".format(name1,name2))
else:
	print("Names are not the same, invalid.")
