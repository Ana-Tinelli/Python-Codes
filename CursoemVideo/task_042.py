a = float(input('Enter the size of size a: ').strip())
b = float(input('Enter the size of size b: ').strip())
c = float(input('Enter the size of size c: ').strip())

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('With the values entered is possible to creat a triangle.')

    if a == b == c:
        print('The triangle is equilateral.')
    elif a == b or a == c or b == c:
        print('The triangle is isosceles.')
    else:
        print('The triangle is scalene.')

else:
    print('With the values entered is NOT possible to create a triangle.')









