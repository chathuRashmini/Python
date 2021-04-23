# STRING OPERATIONS IN PYTHON PART 01

str = 'hello world'
print('string: ', str)
print('Length: ', len(str))
print('Str[1]: ', str[1]) # character in 1st position gets printed
print('str[0:4]', str[0:4]) # 0th index included but 4th index is excluded
# which means characters in 0,1,2,3 get printed
print('str[4:]', str[4:]) # prints 4th and ahead
print('str[:]', str[:]) # prints whole string

if 'l' in str:
    print('l is there') #prints

if 'L' in str:
    print('L is there')
else:
    print('L is NOT there') #prints : case sensitive

if 'm' in str:
    print('m is there')
else:
    print('m is NOT there') #prints
