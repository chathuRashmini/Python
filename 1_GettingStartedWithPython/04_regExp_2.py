# REGULAR EXPRESSIONS PART 02

import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
# [0-9]+ one or more digits in the range 0 to 9
print(y)

z1 = re.findall('[AEIOU]+', x)
print(z1)

z2 = re.findall('[aeiou]+', x)
print(z2)
