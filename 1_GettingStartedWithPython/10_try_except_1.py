score = input("Enter Score: ")
isc = float(score)
try:
    isc = float(score)
except:
    print('Please enter a numeric value')
if isc>0.0:
    if isc>= 0.9:
    	print('A')
    elif isc >= 0.8:
        print('B')
    elif isc >= 0.7:
        print('C')
    elif isc >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Number has to be between 0.0 and 1.0')
