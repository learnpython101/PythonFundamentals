#Example 15
st  = {"apple", "banana", 100, 20.78}

# set cannot support indexing st[1] # set cannot support slicing st[1:]
print (st)
print (type(st))
print (st + st) # set cannot support concatenation
print (st * 2) # set cannot support repetition
# set is immutable st[2] = "hi"