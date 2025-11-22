numbers = []

while True:
    number = int(input('Enter a number: '))
    numbers.append(number)

    question = input('Continue? (y/n): ').strip().lower()
    if question == 'n':
        break
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f'The average is: {average:.2f}')
print(f'The maximum is: {maximum:.2f}')
print(f'The minimum is: {minimum:.2f}')





