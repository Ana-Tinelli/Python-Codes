product_price = float(input('Type the price of the product: £'))
discount = float(product_price * 5) / 100
price_discount = float(product_price - discount)
print('The price of the product after discount is: £{:.2f}'. format(price_discount))
