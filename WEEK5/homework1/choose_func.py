# Task3
# Lesson: Functions as first-class objects



# old function
"""
def choose_func(nums: list, func1, func2):
    increment = 0
    # CAN YOU DO a single line here

    for num in nums:
        if num < 0:
            increment += 1
        else:
            pass

    if increment > 0:
        print(func2(nums))
    else:
        print(func1(nums))

    if increment > 0:
        print(func2(nums))
    else:
        print(func1(nums))
"""

# refactored function
def choose_func(nums: list, func1, func2):
    increment = 0
    for num in nums:
        increment +=1 if num < 0 else 0
    print(func2(nums)) if increment > 0 else print(func1(nums))





# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)

