name = str(input('Enter your full name: '))
find = name.find('Silva')

if find != -1:
     print('Your name contains "Silva".')

else:
     print('Your name does not contain "Silva".')

# or
name = str(input('Enter your full name: '))
print('Has your name Silva: {}'.format('silva' in name.lower()))


