meter = float(input('Type the number of meters: '))
centimeter = (float(meter * 100))
kilometer = (float(meter / 1000))
mile = (float(meter / 1609))
print('{:.2f} meters is igual {:.2f} centimeters'.format(meter, centimeter))
print('{:.2f} meters is igual {:.2f} kilometers'.format(meter, kilometer))
print('{:.2f} meters is igual {:.2f} mile'.format(meter, mile))

