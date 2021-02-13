""""""
"""
List comprehension is an elegant and concise way to create a new list from an existing list in Python.
A list comprehension consists of an expression followed by for statement inside square brackets.

Syntax of the list index() method is:
newlist = [expression for item in iretable (conditional)]
"""
# newlist = [x for x in fruits if "a" in x]

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares = [x * 2 for x in range(10)]
print(squares)

list = [expression for item in iretable]


