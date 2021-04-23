# TUPLE IN PYTHON PART 02

# sorting of a tuple
d = {'y':10, 'z':1, 'c':22, 'p': 10}

# sort by KEY
skey = sorted(d.items())
print('Sorted by key: ', skey)

# sort by VALUE
tmp = list()
for key, val in d.items():
    tmp.append((val, key))
tmp = sorted(tmp, reverse = True) #descending order
print('Sorted by value: ', tmp)
