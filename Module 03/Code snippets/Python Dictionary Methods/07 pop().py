""""""
"""
The pop() method removes and returns an element from a dictionary having the given key.

The syntax of pop() method is
dictionary.pop(key[, default])

pop() Parameters
pop() method takes two parameters:
    - key - key which is to be searched for removal
    - default - value which is to be returned when the key is not in the dictionary

Return value from pop()
The pop() method returns:
    - If key is found - removed/popped element from the dictionary
    - If key is not found - value specified as the second argument (default)
    - If key is not found and default argument is not specified - KeyError exception is raised
"""

# Example 1: Pop an element from the dictionary
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print(f'The popped element is: {element}')
print(f'The dictionary is: {sales}')

# Example 2: Pop an element not present from the dictionary
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava')

# Example 3: Pop an element not present from the dictionary, provided a default value
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'banana')
print(f'The popped element is: {element}')
print(f'The dictionary is: {sales}')

