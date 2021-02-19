""""""
"""
The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.

The syntax of fromkeys() method is:
dictionary.fromkeys(sequence[, value])

fromkeys() Parameters
fromkeys() method takes two parameters:

sequence - sequence of elements which is to be used as keys for the new dictionary
value (Optional) - value which is set to each element of the dictionary

Return value from fromkeys()
fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.

If the value argument is set, each element of the newly created dictionary is set to the provided value.
"""

# Example 1: Create a dictionary from a sequence of keys
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)

# Example 2: Create a dictionary from a sequence of keys with value
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)

# Example 3: Create a dictionary from mutable object list
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

"""
If value is a mutable object (whose value can be modified) like list, dictionary, etc.,
when the mutable object is modified, each element of the sequence also gets updated.

This is because each element is assigned a reference to the same object (points to the same object in the memory).

To avoid this issue, we use dictionary comprehension.
"""

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = {key: list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)

"""`
Here, for each key in keys, a new list from value is created and assigned to it.

In essence, value isn't assigned to the element but a new list is created from it,
which is then assigned to each element in the dictionary.
"""

