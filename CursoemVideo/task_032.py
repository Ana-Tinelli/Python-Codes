year = int(input('Type the year:   ').strip())

if (year % 4 == 0 and
    year % 100 != 0) or (year % 400 == 0):
    print('The year is a leap year.')

else:
    print('The year is not a leap year.')

# to know current day and year
year = int(input('What year to you want to analyse, enter 0 to analise current year:'))
from datetime import date
if year == 0:
    year = date.today().year
print(f'The year is {year}')






