# WEEK3 HOMEWORK2
# Lesson: Dictionaries, for loops, comprehensions

# Tasks2: Calculate the total price of stock from two dictionaries

"""
Action plan:
* define the two dicitionaries
* go through both and multipy the values into a variable
"""
# Get the input dictionaries

# Stock dictionary
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# Price dictionary
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Declare total price variable
total_price = int()

# Declare for that goes through the dict
for key in stock.keys():
	total_price += stock[key] * prices[key]

# Print total value
print(f"Total price of the stock is {total_price}$.") 	
