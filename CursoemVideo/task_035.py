a = float(input('Enter the size of size a: ').strip())
b = float(input('Enter the size of size b: ').strip())
c = float(input('Enter the size of size c: ').strip())

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('With the values entered is possible to creat a triangle.')
else:
    print('With the values entered is NOT possible to create a triangle.')
