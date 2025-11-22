name = 'Ana'
print('\033[4;30;45mHi, World!\033[m')
colours = {'cleaning':'\033[m',
           'red':'\033[31m',
           'green':'\033[32m',
           'black_white':'\033[7:30m',
           'blue':'\033[34m', }

print('Hi! Nice to meet you, {}{}{}!!'.format(colours['red'], name, colours['cleaning']))


