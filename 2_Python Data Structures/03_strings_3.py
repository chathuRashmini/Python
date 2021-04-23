# STRING OPERATIONS IN PYTHON PART 04

up = 'HARRY POTTER'
low = 'harry potter'

upl = up.lower() # converts to lower-case
print('lower case: ', upl)

lowu = low.upper() # converts to upper-case
print('upper case: ', lowu)

auth = 'J. K. Rowling'
print('Author: ', auth)

authtype = type(auth) # gives the datatype of the variable 'auth'
print('Type of auth: ', authtype) # prints -> <class 'str'>

#print('Dir of auth: ', dir(auth))

print('Ro is in: ', auth.find('Ro'))
# checks if 'Ro' is available in 'auth' string
# and if available prints the index of the 'R'

authR = auth.replace('Ro', 'Co')
print('After replacing: ', authR)
# if 'Ro' exists, it is replaced with 'Co'