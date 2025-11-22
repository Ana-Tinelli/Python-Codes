number = input('Enter one four digit number: ')
print(f'The unit is: {number[3]}')
print(f'The ten is: {number[2]}')
print(f'The hundred is: {number[1]}')
print(f'The thousand is: {number[0]}')

#numeric way
num_numeric = int(input('Enter a number: '))
unit = num_numeric // 1 % 10
ten = num_numeric // 10 % 10
hundred = num_numeric // 100 % 10
thousand = num_numeric // 1000 % 10
print('The unit is: {}'.format(unit))
print('The ten is: {}'.format(ten))
print('The hundred is: {}'.format(hundred))
print('The thousand is: {}'.format(thousand))
