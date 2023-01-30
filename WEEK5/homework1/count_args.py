# Week5
# Lesson1: Functions as objects
# Write a function that prints the number of arguments that another function gets


"""
Action plan:
1. Write a simple addititon function with args
2. Make that simple function return the args
3. Feed the args into the count_args function
4. Print the argument count
"""


def count_args(function):
    count_arguments = len(function)
    print(f"The argument count is {count_arguments}.")
    return count_arguments


def add(*args):
    sum(args)
    # return add.__code__.co_nlocals
    return args


count_args(add(2, 3, 5, 7))

"""
What could be improved:
1. You have to make the intial function return args in order for the count_args to work.
2. Take care of the edge cases: Type error when you return sum(args) instead of args
3. Make it work in a more general sense: when we return sum(args)
4. I cannot do len(function.args) in the count_args function
"""

# done but can be better and more general