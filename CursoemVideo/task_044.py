product_price = float(input('Enter the product price: GBP ').strip())
payment_method = int(input('Select the payment method.\n'
                       '1: Cash or Bank Check.\n'
                       '2: Card.\n'
                       '3: Card: 2 parcels.\n'
                       '4: Card: 3 parcels or more.\n'))


if payment_method == 1:
    discount = ((product_price * 10) / 100)
    price = product_price - discount
    print('You have 10% of discount. The product price is GBP {:.2f}.'.format(price))
elif payment_method == 2:
    discount = ((product_price * 5) / 100)
    price = product_price - discount
    print('You have 5% of discount. The  product price is GBP {:.2f}.'.format(price))
elif payment_method == 3:
    print('There is not available discount. Your product price is GBP {:.2f}.'.format(product_price))
elif payment_method == 4:
    interest = (product_price * 20) / 100
    price = product_price + interest
    print('The interest is 20%. Your product price is GBP {:.2f}.'.format(price))
else:
    print('Invalid payment method.')