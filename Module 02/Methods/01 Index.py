""""""
"""
The index() method returns the index of the specified element in the list.

Syntax of the list index() method is:
list.index(element, start, end)

list index() parameters
The list index() method can take a maximum of three arguments:
element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index

Return Value from List index()
The index() method returns the index of the given element in the list.
If the element is not found, a ValueError exception is raised.

Note: The index() method only returns the first occurrence of the matching element.
"""

# Example 1: Find the index of the element

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print(f'The index of e:{index}')

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print(f'The index of i:{index}')

# Example 2: Index of the Element not Present in the List

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('p')
print(f'The index of p:{index}')

# Example 3: Working of index() With Start and End Parameters

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)

"""
Negative indexing
Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])
"""