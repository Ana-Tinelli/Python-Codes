salary = float(input('Enter the salary: £'))
salary_increase = float(salary*15) /100
result = salary + salary_increase
print('The salary of £{:.2f}, after increase 15% is now : £{:.2f} '.format(salary, result))

