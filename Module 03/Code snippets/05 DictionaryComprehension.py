# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)


# This code is equivalent to

squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)


"""
A dictionary comprehension can optionally contain more for or if statements.
An optional if statement can filter out items to form the new dictionary.
Here are some examples to make a dictionary with only odd items.
"""

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

print(odd_squares)
