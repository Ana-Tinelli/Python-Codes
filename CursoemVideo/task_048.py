print('Below are the sum of all odd numbers multiples of 3. Range 1 to 500.')
sum = 0
cont = 0
for c in range (1, 500+1, 2):
   if c % 3 == 0:
       cont = cont + 1
       sum = sum + c
print('The sum of all odd multiples of 3 are: {}'.format(sum))
print('There are {} multiples of 3.'.format(cont))


