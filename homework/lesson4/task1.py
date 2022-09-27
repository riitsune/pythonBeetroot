'''The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement.'''

import random

guess = random.randint(1,10)

i = int(input("try to guess a number"))

if i == guess:
    print("you won!")
else:
    print("you are wrong, the number is ", guess)
    
