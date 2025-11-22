import random
from time import sleep
pc = random.choice (['stone', 'paper', 'scissor'])
player = input('What do you choose?\n' 'stone, paper, or scissor: ').strip().lower()
print('Jo-ken-Po')
sleep(1)
if pc == player:
    print('It is s a tie! Both choose {}!'.format(pc))
elif (pc == 'stone' and player == 'scissor')\
    or (pc == 'paper' and player == 'stone')\
    or (pc == 'scissor' and player == 'paper'):
    print('You are NOT the Winner! The PC choice was {}!'.format(pc))
else:
    print('You are the Winner! The PC choice was {}!'.format(pc))

