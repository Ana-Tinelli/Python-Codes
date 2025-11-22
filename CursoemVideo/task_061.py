print('PA generator.')
print('-=' *10)
first = int(input('First term: '))
common_difference = int(input('PA common difference: '))
term = first
cont = 1

while cont <= 10:
    print('{}'.format(term), end=' ')
    term = term + common_difference
    cont += 1



