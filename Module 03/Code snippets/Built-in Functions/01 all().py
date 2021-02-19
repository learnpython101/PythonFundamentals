""""""
"""
The all() method returns True when all elements in the given iterable are true. If not, it returns False.

The syntax of all() method is:
all(iterable)

all() Parameters
all() method takes a single parameter:
    - iterable - any iterable (list, tuple, dictionary, etc.) which contains the elements

Return Value from all()
all() method returns:
    - True - If all elements in an iterable are true
    - False - If any element in an iterable is false
"""

# Example 1: How all() works for lists?
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

"""
any() method works in a similar way for tuples and sets like lists.
"""

# Example 2: How all() works for strings?
s = "This is good"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))

# Example 3: How all() works with Python dictionaries?
# In case of dictionaries, if all keys (not values) are true or the dictionary is empty,
# all() returns True. Else, it returns false for all other cases..

s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))
