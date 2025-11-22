from random import randint

player = computer = result = c = 0

wins = 0

while True:
    computer = randint(0, 10)
    player = int(input('Enter a number (0-10) to play Evens and Odds: ').strip())
    even_odd = str(input('Do you want to even or odd? ').strip().lower())
    result = player + computer

    if (result %2 == 0 and even_odd == 'even') or (result %2 != 0 and even_odd == 'odd'):
        print(f'You won! The computer choice is {computer}. The result is {result}.')
        wins += 1

    else:
       break

print(f'The computer wins! Player: {player} / Computer: {computer} / Result: {result}')

print(f'Thank you for playing! You won {wins} time(s)!')








