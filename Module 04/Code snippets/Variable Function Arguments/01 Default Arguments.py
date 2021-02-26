""""""
"""
Function arguments can have default values in Python.
We can provide a default value to an argument by using the assignment operator (=)

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
