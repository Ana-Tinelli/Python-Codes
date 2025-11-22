number = int(input('Enter a number: '))
menu = str(input('Select with conversion do you want: \n'
          '1. Convert to binary.\n'
          '2. Convert to octal.\n'
          '3. Convert to hexadecimal.\n'))

if menu == '1':
    print(bin(number))
elif menu == '2':
    print(oct(number))
elif menu == '3':
    print(hex(number))
else:
    print('Invalid input')
