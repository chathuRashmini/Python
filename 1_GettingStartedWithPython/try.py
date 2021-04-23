import re

file = open('try.txt')
numbers = list()
for line in file:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    ylen = len(y)
    j = 0
    while j<ylen:
        x = int(y[j])
        numbers.append(x)
        j = j + 1
tot = 0
i = 0
numbersLen = len(numbers)
while i < numbersLen:
    tot = tot + numbers[i]
    i = i + 1
print(tot)
