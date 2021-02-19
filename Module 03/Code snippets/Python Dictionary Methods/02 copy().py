""""""
"""
They copy() method returns a shallow copy of the dictionary.

The syntax of copy() is:
dict.copy()

copy() Parameters
copy() method doesn't take any parameters.

Return Value from copy()
This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
"""

# Example 1: How copy works for dictionaries?
original = {1:'one', 2:'two'}
new = original.copy()

print(f'Orignal: {original}')
print(f'New: {new}')


"""
Difference in Using copy() method, and = Operator to Copy Dictionaries
When copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.

When = operator is used, a new reference to the original dictionary is created.

Here, when new dictionary is cleared, original dictionary is also cleared.
"""

# Example 2: Using = Operator to Copy Dictionaries
original = {1:'one', 2:'two'}
new = original

# removing all elements from the list
new.clear()

print(f'new: {new}')
print(f'original: {original}')

# Example 3: Using copy() to Copy Dictionaries
original = {1:'one', 2:'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print(f'new: {new}')
print(f'original: {original}')

# Here, when new dictionary is cleared, original dictionary remains unchanged.
