""""""
"""
The len() function returns the number of items (length) in an object.

The syntax of len() is:
len(s)

len() Parameters
s - a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)

Return Value from len()
len() function returns the number of items of an object.

Failing to pass an argument or passing an invalid argument will raise a TypeError exception.
"""

# Example 1: How len() works with tuples, lists and range?
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

# Example 2: How len() works with strings and bytes?
testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))


# Example 3: How len() works with dictionaries and sets?
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
