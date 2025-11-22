distance = float(input('Type how many KM the car has driven: '))
period = int(input('Type how many day the car was rented for: '))
price_distance = float(distance * (15/100))
price_period = int(period * 60)
total_price = price_distance + price_period
print('The total price to pay is: £{:.2f}'.format(total_price))
