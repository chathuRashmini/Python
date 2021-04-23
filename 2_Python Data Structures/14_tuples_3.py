# TUPLE IN PYTHON PART 03

# get most common 10 words from a file

fhand = open('try.txt')
counts = dict()
for line in fhand:
    words = line.split() # get words into a list of elements
    for word in words:
    	# access each elemet (word) in the list
        counts[word] = counts.get(word, 0) + 1
###############################################
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True) # arrange in descending order

for val, key in lst[:10]:
	# goes upto 10 key-value pairs
    print(key, val)
###############################################


# another short method
lst2 = list()
lst2 = sorted([(v, k) for k, v in counts.items()])
print(lst2[len(lst2)-10:])
