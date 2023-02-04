# WEEK5
# Lesson 2: Decorators
# Task 3:
# If some rules' checks returns False:
# the function should return False and print the reason it failed;
# otherwise, return the result;



def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(function):

        def wrapper(argument_type, argument_len, argument_contains):

            def type_str(argument):
                return type(argument) == type(str)

            def lenght_15(argument):
                return len(argument) <= 15

            def contain(argument):
                return 

            type_str(argument_type)
            lenght_15(argument_len)
            def argument




        return wrapper

    return decorator



@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'