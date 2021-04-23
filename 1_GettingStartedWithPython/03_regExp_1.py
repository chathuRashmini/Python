# REGULAR EXPRESSIONS PART 01

import re #need to import 're' library to use regular expressions
file = open('try.txt')
count = 0
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        # checks whether the line has started with 'From:'
        count = count + 1
print(count)

# ^X.*: starts with X, follows any character, any number of
# times, ends with a colon

# ^X-\S+: starts with X, follows with a dash
# follows with a NON white space character, >=1 times
# ends with a colon

sen = 'From: Using the : character:'
x = re.findall('^F.+:', sen) #Greedy
print(x)

y = re.findall('^F.+?:', sen) #NOT greedy
# so gives the shortest one
print(y)
