from datetime import date
today = date.today().year
print('Today is: {}.' .format(today))

birth = int(input('Enter your date of birth DD/MM/YY: '))

age = (today - birth)
print('Your age is:', age)

if age == 18:
 print('You need to list to militar.')

if age < 18:
    time = 18 - age
    print('You do not need to list to militar, yet.\n'
          'You should wait more {} year(s).'.format(time))
if age > 18:
    time = age - 18
    print('You needed to be listed to militar {} year(s) ago.'.format(time))








