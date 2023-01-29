class MyClass:

    @staticmethod
    def some_method():
        print("this method does nothing with self")


def our_decorator(some_funct):
    def wrapper(*args):
        print("something actually meaningful that we want to do before the function")
        some_funct(None, *args)
        print("something actually meaningful that we want to do after the function")
    return wrapper


@our_decorator
def some_function_that_takes_two_parameters(first_param, second_param):
    print(second_param)

some_function_that_takes_two_parameters(5)