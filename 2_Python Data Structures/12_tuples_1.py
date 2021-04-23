# TUPLE IN PYTHON PART 01

# TUPLES are IMMUTABLE (cannot change) you canNOT sort, append, reverse TUPLES
# LISTS => MMUTABLE

l = list()
print('Dir of a list: ',dir(l))

t = tuple()
print('Dir of a tuple: ',dir(t))

(x,y) = (4, 'fred') # it is a tuple on a left hand side
print('x: ', x)
print('y: ', y)

# tuples are COMPARABLE
a = (0, 1, 2)
b = (5, 2, 3)
print('a<b? ', a<b) # true

c = ('Jones', 'Sally')
d = ('Jones', 'Sam')
print('c<d? ', c<d) # true
