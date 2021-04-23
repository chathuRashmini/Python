# STRING OPERATIONS IN PYTHON PART 04

name = '    Edward Cullen   ' # space tabs are there in both sides of the string
print('String: ', name) # prints with the spaces

print('lstrip: ', name.lstrip()) # cuts off the space in left 

print('rstrip: ', name.rstrip()) # cuts off the space in right

print('strip: ', name.strip()) # cuts off the spaces in both sides

print('Strts with E? ', name.startswith('E')) #false
# checks if the given string starts with the given letter
# here prints 'false' hence the name has started with a space
print('Strts with e? ', name.startswith('e')) #false
