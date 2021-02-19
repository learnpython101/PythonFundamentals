""""""
"""
The update() method updates the dictionary with the elements from the another dictionary object
or from an iterable of key/value pairs.

update() method adds element(s) to the dictionary if the key is not in the dictionary.
If the key is in the dictionary, it updates the key with the new value.

The syntax of update() is:
dict.update([other])

update() Parameters
The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
If update() is called without passing parameters, the dictionary remains unchanged.

Return Value from update()
update() method updates the dictionary with elements from a dictionary object or an iterable object of key/value pairs.

It doesn't return any value (returns None).
"""

# Example 1: Working of update()
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

# Example 2: update() When Tuple is Passed
d = {'x': 2}

d.update(y = 3, z = 0)
print(d)
