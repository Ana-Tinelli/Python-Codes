number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))
number_3 = float(input('Enter the third number: '))

if (number_1 > number_2) and (number_1 > number_3):
    print('The first number {} is the greatest.'.format(number_1))
if (number_2 > number_3) and (number_2 > number_1):
    print('The second number is {} is the greatest.'.format(number_2))
if (number_3 > number_1) and (number_3 > number_2):
    print('The third number is {} is the greatest.'.format(number_3))


if (number_1 < number_2) and (number_1 <  number_3):
    print('The first number {} is the smallest.'.format(number_1))
if (number_2 <  number_3) and (number_2 <  number_1):
    print('The second number is {} is the smallest.'.format(number_2))
if (number_3 <  number_1) and (number_3 <  number_2):
    print('The third number is {} is the smallest.'.format(number_3))
