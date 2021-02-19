""""""
"""
The setdefault() method returns the value of a key (if the key is in dictionary).
If not, it inserts key with a value to the dictionary.

The syntax of setdefault() is:
dict.setdefault(key[, default_value])

setdefault() Parameters
setdefault() takes a maximum of two parameters:

key - the key to be searched in the dictionary
default_value (optional) - key with a value default_value is inserted to the dictionary if the key is not in the dictionary.
If not provided, the default_value will be None.
Return Value from setdefault()
setdefault() returns:

value of the key if it is in the dictionary
None if the key is not in the dictionary and default_value is not specified
default_value if key is not in the dictionary and default_value is specified
"""

# Example 1: How setdefault() works when key is in the dictionary?
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print(f'person = {person}')
print(f'Age = {age}')

# Example 2: How setdefault() works when key is not in the dictionary?
person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print(f'person = {person}')
print(f'salary = {salary}')

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print(f'person = {person}')
print(f'age = {age}')
