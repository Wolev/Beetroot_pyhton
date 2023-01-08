#Task2: Check if string is a 10 digit number

import re

phone_number = input("Input your phone number:")

phone_number_check = re.search("^[0-9]{10}$", phone_number)

if phone_number_check is None:
	print("{} is NOT a valid phone number.".format(phone_number))
else:
	print("{} is a VALID phone number.".format(phone_number))
