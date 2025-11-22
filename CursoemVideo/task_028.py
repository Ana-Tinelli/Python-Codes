import random
numbers_range = (0, 5)
computer_choice = random.choice(numbers_range)
user_choice = (int(input('Try to guess, enter one number between 0 to 5: ').strip()))

if user_choice == computer_choice:
    print('You guessed the number!')
else:
    print('Sorry, you did not guess the right number, the number was {}'.format(computer_choice))

#or

from random import randint

computer = randint(0, 5)
gamer = int(input('Enter one number between 0 and 5: ').strip())

if gamer == computer:
    print('You guessed the number!')
else:
    print('Sorry, you did not guess the right number, the number was {}'.format(computer_choice))




