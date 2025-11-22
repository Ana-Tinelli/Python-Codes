name = str(input('Type your full name:').strip())
name_split = name.split()

print(f'Your first name is: {name_split[0]}')
print(f'Your last name is: {name_split[-1]}')