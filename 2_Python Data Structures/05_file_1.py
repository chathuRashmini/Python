# FILE HANDLING IN PYTHON PART 01

file = open('try.txt')
print(file)
# can give a opening mode like open('try.txt', 'r')
# r - read only

linecount = 0
for line in file:
    #line refers to a single line in a code
    print(line)
    linecount = linecount + 1
print(linecount)
