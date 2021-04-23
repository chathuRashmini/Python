# STRING OPERATIONS IN PYTHON PART 02
# focuses on ASCII values of the characters

word = 'Edward'

if word < 'edward':
    print('Edward < edward') #true because ASCII value of 'E' < ASCII value of 'e'
else:
    print('Edward > edward')

if word < 'Bella':
    print('Edward < Bella') #true
    # because output depends on the ASCII value of the first character of the comparing strings
else:
    print('Edward > Bella')
