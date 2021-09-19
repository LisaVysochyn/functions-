'''Generate a random number between 1 and 10.
Ask the user to guess the number and print
a message based on whether they get it right or not.'''

from random import *

x = randint(1,10)
number = int(input('Guess the number from 1 to 10: '))

if number<1 or number>10:
    print('The entry is invalid!')
elif number == x:
    print('You win!')
else:
    print('You lose!')
