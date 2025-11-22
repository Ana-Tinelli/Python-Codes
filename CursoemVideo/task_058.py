
from random import randint

computer = randint(0, 10)
times = 0

gamer = int(input('Enter one number between 0 and 10: ').strip())

while gamer != computer:
      gamer = int(input('Enter one number between 0 and 10: ').strip())
      times += 1
      if gamer == computer:
          print('You guessed the number!')

print('You needed to type {} times, before you guess.'.format(times))

print('Congrats!')



