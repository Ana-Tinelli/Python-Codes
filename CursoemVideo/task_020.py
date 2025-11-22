from random import shuffle
n1 = input('Enter the first name: ')
n2 = input('Enter the second name: ')
n3 = input('Enter the third name:')
n4 = input('Enter the fourth name: ')
list = [n1, n2, n3, n4]
mix = shuffle(list)
print('The sequence for presentation is: ')
print(list)
