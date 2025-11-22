house = float(input('Enter how much is the house price: GBP ').strip())
salary = float(input('Enter how much is your salary: GBP ').strip())
years = float(input('Enter how many years will you pay the mortgage: ').strip())
parcel_value = (house / years) / 12

percentage_30 = (salary * 30) / 100


if parcel_value <= percentage_30:
    print('Your mortgage is approved, your parcel will be around GBP {:.2f}'.format(parcel_value))
else:
    print('In this condition, the parcel will be higher than 30% of your salary - GBP {:.2f}.\n'
          'Your current condition allow you a maximum parcel of GBP {:.2f}.\n'
          'You can increase the number of years or your salary.'.format(parcel_value, range))





