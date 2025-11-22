

pa = (input('Type the arithmetic progression number: '))
pa = [int(x) for x in pa.split(',')]

a_1 = pa[0]
common_difference = pa[1] - pa[0]

print ('The first term is this PA is {}'.format(a_1))
print ('The common difference is {}'.format(common_difference))

first_terms = pa[0:11]
print('The first 10 terms: {}'.format(first_terms))


