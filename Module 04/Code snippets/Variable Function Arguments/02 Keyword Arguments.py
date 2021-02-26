""""""
"""
When we call a function with some values, these values get assigned to the arguments according to their position.

For example, in the below function greet(), when we call it as greet("Bruce", "How do you do?"),
the value "Bruce" gets assigned to the argument name and similarly "How do you do?" to msg.

Python allows functions to be called using keyword arguments.
When we call functions in this way, the order (position) of the arguments can be changed. 

Following calls to the below function are all valid and produce the same result.

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")           
As we can see, we can mix positional arguments with keyword arguments during a function call.
But we must keep in mind that keyword arguments must follow positional arguments.

Having a positional argument after keyword arguments will result in errors.
For example, the function call as follows:

greet(name="Bruce","How do you do?")
Will result in an error:
SyntaxError: non-keyword arg after keyword arg

"""


def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print(f"Hello {name},{msg}")


greet("Kate")
greet("Bruce", "How do you do?")