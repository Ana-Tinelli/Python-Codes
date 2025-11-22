salary = float(input('What is the salary of the employee: GBP ').strip())


if salary <= 1250:
    salary = ((salary * 15) /100) + salary
    print('The salary with 15% of increase is: GBP {:.2f}'.format(salary))
else:
    salary = ((salary * 10) / 100) + salary
    print('The salary with 10% of increase is: GBP {:.2f}'.format(salary))
