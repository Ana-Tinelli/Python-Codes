weight = float(input('Enter your weight in Kg: ').strip())
height = float(input('Enter you height in meters: ').strip())

imc = weight /(height * height)
print('Your IMC is: {:.2f}'.format(imc))

if imc < 18.5:
    print('You are underweight.')
elif 18.5 <= imc < 25:
    print('Your weight is ideal.')
elif 25 <= imc < 30:
    print('You are overweight.')
elif 30 <= imc < 40:
    print('Your IMC shows obesity.')
elif imc >= 40:
    print('You are clinically obese.')


