number = int(input('Enter a number: '))
total = 0

for c in range (1, number + 1):
    if number % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('The number {} was divided {} times.'.format(number, total))
if total == 2:
    print('Number is prime.')
else:
    print('Number is not prime.')
