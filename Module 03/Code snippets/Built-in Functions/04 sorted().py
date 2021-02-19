""""""
"""
The sorted() function returns a sorted list from the items in an iterable.

The sorted() function sorts the elements of a given iterable in a specific order
(either ascending or descending) and returns the sorted iterable as a list.

The syntax of the sorted() function is:
sorted(iterable, key=None, reverse=False)

Parameters for the sorted() function
sorted() can take a maximum of three parameters:
    - iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
    - reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
    - key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.
"""

# Example 1: Sort string, list, and tuple
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

"""
Notice that in all cases that a sorted list is returned.
Note: A list also has the sort() method which performs the same way as sorted().
The only difference is that the sort() method doesn't return any value and changes the original list.
"""

# Example 2: Sort in descending order
# The sorted() function accepts a reverse parameter as an optional argument.
# Setting reverse = True sorts the iterable in the descending order.

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))

# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))
