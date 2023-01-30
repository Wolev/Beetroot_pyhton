# This is the first program but tried with the inspect module
# News flash: it doesn't work
# Question: why does it fail?

"""
Programming problem:
I can't debug this code because it gives errors in:
* File "/usr/lib/python3.10/inspect.py", line 3250, in signature
* File "/usr/lib/python3.10/inspect.py", line 2998, in from_callable
*  File "/usr/lib/python3.10/inspect.py", line 2395, in _signature_from_callable

Questions:
1. How do I understand the library code so my I can modify my user code effectively?
"""


import inspect

def count_args(function):
    return len(inspect.signature(function).parameters)

def add(arg1, arg2):
    return arg1, arg2


count_args(count_args(add(1,2)))
