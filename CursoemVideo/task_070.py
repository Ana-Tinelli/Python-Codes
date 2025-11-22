total = total_over_1000 = cheaper = cont = name_cheapest = 0
while True:
    product_name = str(input('What is the product name? ').strip())
    product_price = float(input('What is the product price? ').strip())
    cont += 1
    total += product_price
    if product_price >1000:
        total_over_1000 += 1
    if cont == 1:
        cheaper = product_price
        name_cheapest = product_name
    else:
        if product_price < cheaper:
            name_cheapest = product_name

    reply = ' '
    while reply not in 'YN':
        reply = str(input('Do you want to continue (Y/N): ').strip().upper()[0])
    if reply == 'N':
        break
print('{:-^40}'.format('Finished!'))
print(f'The purchase total is: GBP {total:.2f}')
print(f'There are {total_over_1000} product(s) over than GBP 1000.00')
print(f'The cheapest product is: {name_cheapest} the price is GBP {cheaper:.2f}')



