print('=' * 40)
print('{:-^40}'.format('Tinelli Bank'))
print('=' * 40)

amount = int(input('How much money do you want withdraw? GBP '))
total = amount
banknote = 50
total_banknote = 0

while True:
    if total >= banknote:
        total -= banknote
        total_banknote += 1
    else:
        if total_banknote > 0:
         print(f'Total {total_banknote} banknotes of {banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1


        total_banknote = 0
        if total == 0:
            break














