""""""

"""
The append() method adds an item to the end of the list.

Syntax 
list.append(item)

append() Parameters
The method takes a single argument

item - an item to be added at the end of the list
The item can be numbers, strings, dictionaries, another list, and so on.

Return Value from append()
The method doesn't return any value (returns None).
"""

# Example 1: Adding Element to a List

# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print(f'Updated animals list:{animals}')


# Example 2: Adding List to a List

# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to the animals list
animals.append(wild_animals)

print(f'Updated animals list:{animals}')


"""
It is important to notice that, a single item (wild_animals list) is added to the animals list in the above program.

If you need to add items of a list to another list (rather than the list itself), use the extend() method.
"""