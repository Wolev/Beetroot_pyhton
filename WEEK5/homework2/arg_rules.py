# WEEK5
# Lesson 2: Decorators
# Task 3:
# If some rules' checks returns False:
# the function should return False and print the reason it failed;
# otherwise, return the result;


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(function):

        def wrapper(string: str) -> str:
            """
            -> str is a type hint.
            a type hint specifies the return type of the function in Python
            helps the IDE provide better code analysis suggest auto-completion options
            """
            # if type is not string print statement and return False
            if not isinstance(string, type_):
                """
                type_ is a parameter in the arg_rules decorator
                type_ specifies the type of the argument that the decorated function is expecting
                type_ is string in this case 
                """
                print(f"Expected {type_}, but got {type(string)}.")
                return False

            # if length of string is bigger that max_length print statement and return False
            if len(string) > max_length:
                print(f"The length of {string} is bigger than {max_length}.")
                return False

            # if symbol not in string print statement and return False
            for symbol in contains:
                if symbol not in string:
                    print(f"The {symbol} symbol is not found in {string}.")
                    return False

            # if all checks passed return function(string)
            return function(string)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
print("The assert is False\n")

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
print(create_slogan('S@SH05'))
