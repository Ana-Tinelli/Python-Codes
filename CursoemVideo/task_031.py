km = float(input('Enter the distance of the journey in KM: '))

if km <= 200:
    cost = km * 0.50

else:
    cost = km * 0.45

print(f'The cost is GBP {cost:.2f}')





