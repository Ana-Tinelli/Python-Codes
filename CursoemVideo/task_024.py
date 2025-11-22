city = str(input('Enter the city name: ')).strip()
found = city.find('SANTO')
# when use upper case, it considers upper and lower inputs.


if found == 0:
    print('The city starts with "Santo": True')
else:
    print('The city starts with "Santo": False')

# or
city = str(input('Enter the city name: ')).strip()
print(city[:5].upper() == 'SANTO')




