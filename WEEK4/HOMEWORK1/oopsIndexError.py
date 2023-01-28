# WEEK4
# Task1: Create a function that raises an index error
# Create a function that calls the oops function
# Comment to create pull request

def oops(iterable, index):
    try:
        print(f"The contents of your variable: {iterable}")
        print(f"The index requested is: {index}")
        print(f"The element from the iterable data type is: {iterable[index]}")
    except IndexError:
        print("The index is bigger than the number of elements in the iterable data type.")
    except KeyError:
        print("Your dictionary/set index is bigger than the number of elements.")

def catch_oops(iterable, index):
    try:
        oops(iterable, index)
    except Exception:
        print(f"Is this {iterable}, an iterable data type?")
        print("Try feeding this function with better data.")

if __name__ == "__main__":
    list = [1,2,3]
    dict = {1:"1"}
    catch_oops(1,1)
    catch_oops(list, 12)
