number = int(input('Enter a number to have the multiplication table: ').strip())

for c in range (0, 11):
    result = number * c
    print('{} x {} = {}'.format(number, c, result))

