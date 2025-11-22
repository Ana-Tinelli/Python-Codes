from datetime import date
today = date.today().year
birth_year = int(input('Enter your birth year YYYY: '))
age = today - birth_year
print('Your age is: {}'.format(age))

if age <= 9:
    print('You are Children!')
elif age <= 14:
    print('You are Kid!')
elif  age <= 19:
    print('You are Junior!')
elif  age <= 20:
    print('You are Senior!')
else:
    print('You are Master!')


