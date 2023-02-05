# Create a decorator that does something before the function runs and after it runs
# Let's start with print "begin" and "end"

# function = decorator(function)


def my_decorator(function):

    print("begin")
    function()
    print("end\n")
    return function



@my_decorator
def some_function():
    print("A big program.")
    return None

@my_decorator
def some_other_function():
    print("A bigger program.")
    return None

some_function()
some_other_function()