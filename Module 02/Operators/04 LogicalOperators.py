"""
These are conjunctions that you can use to combine more than one condition.
We have three Python logical operator – and, or, and not that come under python operators.
"""

"""
1. and Operator in Python
If the conditions on both sides of the operator are True, then the expression as a whole is True.

2. or Operator in Python
The expression is false only if both the statements around the operator are false. Otherwise, it is true.
‘and’ returns the first False value or the last value; ‘or’ returns the first True value or the last value

3. not Operator in Python
This inverts the Boolean value of an expression. It converts True to False, and False to True.
As you can see below, the Boolean value for 0 is False. So, not inverts it to True.

"""

# 1
a = 7>7 and 2>-1

# 2
a = 7>7 or 2>-1
7 and 0 or 5

# 3
a = not(0)
