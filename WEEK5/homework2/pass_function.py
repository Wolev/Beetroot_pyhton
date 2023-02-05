# WEEK5
# Lesson 2: Decorators
# Task1 needs to do the following:
# Make the logger function print the following message:
# {name_of_function} called with arg1, arg2, ..arg_n


def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {', '.join([str(arg) for arg in args])}")
    return wrapper


# @logger is the same as add = logger(add)
@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1, 2, 3)
