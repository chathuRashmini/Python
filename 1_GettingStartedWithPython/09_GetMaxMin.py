num = [3, 12, 9, 41, 15, 74]

maxnum = -1 # assume maximum number as -1

for n in num:
    if n >= maxnum:
        maxnum = n
print('Maximum number = ', maxnum)

# this will print the maximum number among the numbers in the 'num' list
# however the negative side of this is if any number is a negative number,
# the code is not accurate enough to find the maximum
# solution is as follows

numarr = [19, 41, 12, 3, 74, 15]

minnum = None # minimum is initialized as 'not seen'

for num in numarr:
    if minnum is None:
        minnum = num
    else:
        if minnum > num:
            minnum = num
print('Minimum number = ', minnum)
