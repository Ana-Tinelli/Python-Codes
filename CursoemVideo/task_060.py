from math import factorial
n = int(input('Enter a number: '))
c = n
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    c -= 1
f = factorial(n)
print('The factorial of {} is {}'.format(n, f))


# or

result = 1
factor = 1

number = int(input('Enter a number to see the factorial: ').strip())

while factor <= number:
   result *= factor
   factor += 1
print('The result is: {}'.format(result))












