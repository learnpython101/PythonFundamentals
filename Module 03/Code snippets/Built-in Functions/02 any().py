""""""
"""
The any() function returns True if any element of an iterable is True. If not, any() returns False.

The syntax of any() is:
any(iterable)

Parameters for the any() function
The any() function takes an iterable (list, string, dictionary etc.) in Python.

Value Returned by the any() function
The any() function returns a boolean value:
    - True if at least one element of an iterable is true
    - False if all elements are false or if an iterable is empty
"""

# Example 1: Using any() on Python Lists
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))

# Example 2: Using any() on Python Strings
# Atleast one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))

# Example 3: Using any() with Python Dictionaries
# In the case of dictionaries, if all keys (not values) are false or the dictionary is empty,
# any() returns False. If at least one key is true, any() returns True.

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))