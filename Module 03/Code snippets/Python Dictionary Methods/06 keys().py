""""""
"""
The keys() method returns a view object that displays a list of all the keys in the dictionary

The syntax of keys() is:
dict.keys()

keys() Parameters
keys() doesn't take any parameters.

Return Value from keys()
keys() returns a view object that displays a list of all the keys.

When the dictionary is changed, the view object also reflects these changes.
"""

# Example 1: How keys() works?
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

# Example 2: How keys() works when dictionary is updated?
person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)

"""
Here, when the dictionary is updated, keys is also automatically updated to reflect changes.
"""
