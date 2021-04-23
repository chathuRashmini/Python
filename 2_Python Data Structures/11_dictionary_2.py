# PYTHON DICTIONARIES PART 02

names = ['edward', 'bella', 'jacob', 'edward', 'alice', 'edward', 'bella', 'edward', 'rosalie']

count = dict()

for name in names:
	# for loop is used to count the number of occurences of each element in the above list
    if name not in count:
    	# if the name is not a key in the dictionary add it
        count[name] = 1
    else:
    	# if name is already a key, then increment its value
        count[name] = count[name] + 1
print(count)

x = count.get('edward', 0) #get value of the key 'edward' if it exists
print('value of edward: ', x)

y = count.get('charlie', 0) #gives 0 if the key 'charlie' is not there
print('value of charlie: ', y)

print('All the keys in the dictionary: ')
for key in count:
    print(key)

print('All the items in the dictionary: ', count.items()) # type-> dictionary

print('All the key value pairs in the dictionary: ')
for key, val in count.items():
    print(key, val)

print('All the values in the dictionary: ')
print(count.values())
