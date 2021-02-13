""""""
"""
The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

Syntax of the extend() method is:
list.extend(iterable)

Here, all the elements of iterable are added to the end of list.

extend() Parameters
As mentioned, the extend() method takes an iterable such as list etc

Return Value from extend()
The extend() method modifies the original list.
It doesn't return any value.
"""

# Example 1: Using extend() Method

# languages list
languages = ['Sesotho', 'English']

# another list of language
languages1 = ['Xhosa', 'Setswana']

# appending language1 elements to language
languages.extend(languages1)

print(f'Languages List:{languages}')


# Example 2: Add Elements of Tuple and Set to List

# languages list
languages = ['Sesotho']

# languages tuple
languages_tuple = ('Xhosa', 'Setswana')

# languages set
languages_set = {'Zulu', 'Afrikaans'}

# appending language_tuple elements to language
languages.extend(languages_tuple)

print(f'New Language List:{languages}')

# appending language_set elements to language
languages.extend(languages_set)

print(f'Newer Languages List:{languages}')

"""
Other Ways to Extend a List
You can also append all elements of an iterable to the list using:

1. the + operator

a = [1, 2]
b = [3, 4]

a += b    # a = a + b

# Output: [1, 2, 3, 4]
print('a =', a)
Output

a = [1, 2, 3, 4]
2. the list slicing syntax

a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)
Output

a = [1, 2, 3, 4]
Python extend() Vs append()
If you need to add an element to the end of a list, you can use the append() method.

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)
"""
