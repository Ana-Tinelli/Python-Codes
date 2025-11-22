
phrase = str(input('Type one phrase: '))
a_counter = phrase.lower().count('a')
print(f'The phase has {a_counter} letter(s) "a". ')


#or
phrase = str(input('Type one phrase: ')).upper().strip()
print('The letter A appears {} time(s) in this phrase.'.format(phrase.count('A')))
print('The first letter A appears at position {}.'.format(phrase.find('A')+1))
print('The last letter A appears at position {}.'.format(phrase.rfind('A')+1))



