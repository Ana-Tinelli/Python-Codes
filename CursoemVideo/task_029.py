car_speed = float(input('Enter the car speed in Km/h:  ').strip())
penalty = float(car_speed - 80) * 7
if car_speed > 80:
    print('Sorry, the speed is too high, the penalty to pay is: GBP {:.2f}'. format(penalty))
else:
    print('Well done, the car speed is between the allowed value!')



