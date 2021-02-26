""""""
"""
Syntax of Lambda Function in python
lambda arguments: expression

Lambda functions can have any number of arguments but only one expression.
The expression is evaluated and returned. 
Lambda functions can be used wherever function objects are required.

"""

double = lambda x: x * 2

print(double(5))


"""def double(n):
    return n * 2


print(double(5))
"""

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)
