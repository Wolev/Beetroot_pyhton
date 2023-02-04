# WEEK5
# Lesson 2: Decorators
# Task 2:
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function.
# Warning!
# This problem is very challenging and needs to be explained in class, Roman.

"""
Action plan:
1. Create a decorator function inside the stop_words function to pass create_slogan as argument
2. Create a wrapper function inside the decorator function to pass the name as argument
3. The name argument is a tuple and needs to be transformed into a correct string, like so:
        (Steve, ) need to be converted to "Steve"
4. Iterate through the list of words and change them into *
5. return result for wrapper, return wrapper for decorator, return decorator for stop words
6. After assert you should print the function to display the result, like so:
        print(create_slogan("Steve"))

"""


# This problem is very hard and needs to be explained in class, Roman!
# Made it pretty by fixing all the style problems.


def stop_words(words: list):
    def decorator(function):
        # The function passed to the decorator is create_slogan

        def wrapper(function_argument):
            # the argument passed to wrapper is name
            # The result of this is from "" to "Steve,"
            result = "".join(function(function_argument))
            # Replace "Steve," with "Steve"
            result = result.replace(",", "")
            # Use for to go into the list of words: ['pepsi', 'BMW']
            for word in words:
                # replace word with *
                result = result.replace(word, '*')
            # return result for wrapper
            return result

        # return wrapper for decorator
        return wrapper

    # return decorator for stop_words
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name}, drinks pepsi in his brand new BMW!"


# If to assert is True, the next line of code is printed
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))
print()
