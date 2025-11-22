from random import choice
names = (input('Enter the names separated by commas: ')).split(',')
chosen = choice(names)
print('The name choose is: {}'.format(chosen.strip()))


n1 = input('Enter the first name: ')
n2 = input('Enter the second name: ')
n3 = input('Enter the third name:')
n4 = input('Enter the fourth name: ')
list = [n1, n2, n3,n4]
chosen = choice(list)
print('The chosen name is: {}'.format(chosen))






