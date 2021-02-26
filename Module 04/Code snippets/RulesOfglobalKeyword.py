""""""
"""
The basic rules for global keyword in Python are:

    1. When we create a variable inside a function, it is local by default.
    2. When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
    3. We use global keyword to read and write a global variable inside a function.
    4. Use of global keyword outside a function has no effect.
    
"""

# Accessing global Variable From Inside a Function
c = 1  # global variable


def add():
    print(c)


add()

"""# Modifying Global Variable From Inside the Function
c = 1  # global variable


def add():
    c = c + 2  # increment c by 2
    print(c)


add()
"""

"""# Changing Global Variable From Inside a Function using global
c = 0  # global variable


def add():
    global c
    c = c + 2  # increment by 2
    print("Inside add():", c)


add()
print("In main:", c)
"""

