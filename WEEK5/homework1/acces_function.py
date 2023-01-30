# Week5
# Lesson1: Functions as objects
# Write a function in which another function is accesed
# return a function

"""
Action plan:
1. Write an outer_function
2. Print a message for location purposes
3. Write an inner_function
4. Print smth
5. Have an outsider function try to get in on the fun
"""

def outer():  #Outer function
    msg = 'I belong to the outer function '
    def inner(): #Nested function
        print ("This message comes from the inner function.")
    return inner


call_function = outer()
call_function()