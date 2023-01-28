# WEEK4
# Task2: catch some excepts for a math expression
# Types of errors to catch: ZeroDivisionError and TypeError
# Comment for the pull request

def square_divide(first, second):
    try:
        print(f"{(int(first) ** 2) / int(second)}")
    except ZeroDivisionError:
        print("The second element is {second}. Don't divide by zero")
        second = input("Try again: ")
        return square_divide(first, second)
    except ValueError:
        print("The data type is not an int. Try again: ")
        first = input("The first element: ")
        second = input("The second element: ")
        return square_divide(first, second)

if __name__ = "__main__":
	a = input("Input the first element: ")
	b = input("Input the second element: ")
	square_divide(a,b)
