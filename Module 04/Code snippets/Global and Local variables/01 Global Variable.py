x = "global"


def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

"""
In the above code, we created x as a global variable and defined a foo() to print the global variable x.
Finally, we call the foo() which will print the value of x.
"""

# What if you want to change the value of x inside a function?
"""x = "global"

def foo():
    x = x * 2
    print(x)

foo()"""