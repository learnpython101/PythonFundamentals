# Here is an example to illustrate the scope of a variable inside a function.

def my_func():
    x = 10
    print(f"Value inside function:{x}")


x = 20
my_func()
print(f"Value outside function:{x}")

"""
Here, we can see that the value of x is 20 initially. 
Even though the function my_func() changed the value of x to 10, it did not affect the value outside the function.

This is because the variable x inside the function is different (local to the function) from the one outside. 
Although they have the same names, they are two different variables with different scopes.

On the other hand, variables outside of the function are visible from inside. They have a global scope.

We can read these values from inside the function but cannot change (write) them. 
In order to modify the value of variables outside the function, 
they must be declared as global variables using the keyword global.
"""
