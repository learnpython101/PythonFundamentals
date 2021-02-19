""""""
"""
The values() method returns a view object that displays a list of all the values in the dictionary.

The syntax of values() is:
dictionary.values()

values() Parameters
values() method doesn't take any parameters.

Return value from values()
values() method returns a view object that displays a list of all values in a given dictionary.
"""

# Example 1: Get all values from the dictionary
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())

# Example 2: How values() works when dictionary is modified?
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

values = sales.values()
print(f'Original items: {values}')

# delete an item from dictionary
del[sales['apple']]
print(f'Updated items: {values}')

"""
The view object values doesn't itself return a list of sales item values 
but it returns a view of all values of the dictionary.

If the list is updated at any time, the changes are reflected on the view object itself,
as shown in the above program.
"""
