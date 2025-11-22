n = m = r = j = 0

while n >= 0:
    n = int(input('Enter a number do see the multiplication table: ').strip())

    if n <= 0:
        print('Enter a positive number.')
        break

    print('The multiplication table is:')
    for j in range(0, 11):
        print(f'{n} * {j} = {n * j}')




