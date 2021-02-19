""""""
"""
The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.

The syntax of popitem() is:
dict.popitem()

Parameters for popitem() method
The popitem() doesn't take any parameters.

Return Value from popitem() method
The popitem() method removes and returns the (key, value) pair from the dictionary
in the Last In, First Out (LIFO) order.
    - Returns the latest inserted element (key,value) pair from the dictionary.
    - Removes the returned element pair from the dictionary.
    - Note: Before Python 3.7,
      the popitem() method returned and removed an arbitrary element (key, value) pair from the dictionary.
"""

# Example: Working of popitem() method
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print(f'Return Value = {result}')
print(f'person = {person}')

# inserting a new element pair
person['profession'] = 'Plumber'

# now ('profession', 'Plumber') is the latest element
result = person.popitem()

print(f'Return Value = {result}')
print(f'person = {person}')

"""
Note: The popitem() method raises a KeyError error if the dictionary is empty.
"""