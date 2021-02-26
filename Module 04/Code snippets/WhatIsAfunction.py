""""""
"""
Syntax of Function
def function_name(parameters):
    ""docstring""
    statement(s)
    
Above shown is a function definition that consists of the following components.

1. Keyword def that marks the start of the function header.
2. A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon (:) to mark the end of the function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
7. An optional return statement to return a value from the function.

"""

# Example of a function


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print(f"Hello, {name}. Good morning!")


greet("Letlaka")
