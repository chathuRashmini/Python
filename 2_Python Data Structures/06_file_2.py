# FILE HANDLING IN PYTHON PART 01

#handle = open('try.txt', 'r')
file = open('try.txt')
file1 = file.read()
print('File length: ', len(file1))
print('file1[:20]', file1[:20]) 
# prints first 20 letters
