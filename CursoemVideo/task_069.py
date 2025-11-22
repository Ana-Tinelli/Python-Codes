people_over_18 = 0
total_men = 0
women_under_20 = 0

while True:
    age = int(input('Enter your age: ').strip())
    gender = str(input('Enter your gender (F/M): ').strip().lower())

    if age > 18:
        people_over_18 += 1

    if gender == 'm':
        total_men += 1

    if gender == 'f' and age <20:
        women_under_20 += 1

    again = str(input('Do you want to continue (Y/N): ').strip().lower())
    if again == 'n':
            break

print(f'It was registered {people_over_18} people over 18 years old.')
print(f'It was registered {total_men} men in the total.')
print(f'It was registered {women_under_20} women under 20 years old.')


