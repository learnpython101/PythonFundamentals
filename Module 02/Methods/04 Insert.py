""""""
"""
The list insert() method inserts an element to the list at the specified index.

Syntax of the insert() method is
list.insert(i, elem)

Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.

insert() Parameters
The insert() method takes two parameters:

index - the index where the element needs to be inserted
element - this is the element to be inserted in the list

Notes:
If index is 0, the element is inserted at the beginning of the list.
If index is 3, the element is inserted after the 3rd element. Its position will be 4th.

Return Value from insert()
The insert() method doesn't return anything; returns None.
It only updates the current list.
"""

# Example 1: Inserting an Element to the List

# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print(f'Updated List:{vowel}')


# Example 2: Inserting a Tuple (as an Element) to the List

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print(f'Updated List:{mixed_list}')
