# PYTHON LISTS PART 01

fruits = list() #create a new list
print('Type: ', type(fruits)) # <class list>

fruits.append('strawberries') #add to the end of the list
fruits.append('mango')
fruits.append('banana')
fruits.append('oranges')
print('fruits: ', fruits)

print('mango in fruits', 'mango' in fruits) # true
# checks whether 'mango' exists in the list 'fruits'

print('guava not  in fruits', 'guava' not in fruits) # true
# checks whether 'mango' does NOT exists in the list 'fruits'
