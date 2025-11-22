from datetime import date
birth_year = 0
age = 0
quantity_more = 0
less = 0

for c in range (0, 7, 1):
    birth_year = input('Please enter your birth year (YYYY): ')
    age = date.today().year - int(birth_year)
    if age >=18:
        quantity_more += 1
    else:
        less += 1
print('There are {} people more than 18 years old, and {} less than 18 years old.'.format(quantity_more, less))

