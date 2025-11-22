num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))
menu = 0

while menu != 5:
 menu = (int(input('Select the option you need:\n'
      '[1] Sum\n'
      '[2] Multiplication\n'
      '[3] Biggest number\n'
      '[4] New number\n'
      '[5] Exit\n')))

 if menu == 1:
    print(f'The result is {num_1 + num_2}')
 elif menu  == 2:
    print(f'The result is {num_1 * num_2}')
 elif menu  == 3:
    print(f'The {max(num_1, num_2)} is the biggest number.')
 elif menu  == 4:
    num_1 = int(input('Enter the first new number: '))
    num_2 = int(input('Enter the second new number: '))
 elif menu  == 5:
    print('Exit.')
 else:
     print('Invalid input.')








