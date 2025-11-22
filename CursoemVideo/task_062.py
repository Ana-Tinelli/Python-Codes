print('PA generator.')
print('-=' *10)
first = int(input('First term: '))
common_difference = int(input('PA common difference: '))
term = first
cont = 1
total = 0
more = 10
while more != 0:
 total = total + more
 while cont <= total:
    print('{}'.format(term), end=' ')
    term = term + common_difference
    cont += 1
 print('Pause')
 more = int(input('How many terms do you want to show: '))
print('Progression with {} terms.'.format(total))
print('PA generator.')
print('-=' *10)




