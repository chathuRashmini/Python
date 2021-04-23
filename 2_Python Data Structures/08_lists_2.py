# PYTHON LISTS PART 02

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

print('a: ', a)
print('Lenth of a: ', len(a)) # number of elements in the given list
print('Max of a: ', max(a)) # maximum number among the elements
print('Min of a: ', min(a)) # minimum number among the elements
print('Sum of a: ', sum(a)) # summation of the values of all the elements

print('a+b', a + b) #addition

print('a[2:]', a[2:]) # slicing the list from index 2 inclusively

names = ['edward', 'jacob', 'bella', 'alice', 'rosalie']
names.sort() #sorting the list
print('Sorted names: ', names)
