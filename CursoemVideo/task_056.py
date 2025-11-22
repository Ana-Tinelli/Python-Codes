
name = 0
age = 0
gender = 0
oldest_man = 0
women_under_20 = 0
max_age = 0
average = 0
total_age = 0

for i in range (4):
    name = input(f'Enter your name {i+1}: ').strip()
    age = int(input(f'Enter your age {i+1}: ').strip())
    gender = input(f'Enter your gender (F/M) {i+1}: ').strip().upper()

    total_age += age

    if gender == 'M' and age > max_age:
      oldest_man = name
      max_age = age

    if gender == 'F' and age < 20:
        women_under_20 += 1

average = total_age / 4


print('The oldest man is {}, he is {} years old.'.format(oldest_man, max_age))
print('There is/are {} woman/women under 20 years old.'.format(women_under_20))
print('The average age is {} years old.'.format(average))




