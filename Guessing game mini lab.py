'''
9/8
Aditya Chakraborty
Guessing Game Mini-Lab
'''


import random

print("Welcome to the guessing game")

randomnumber = random.randint(1,100)

guess = input("I have picked a number\nWhat do you think the number is: ")
guess = int(guess)

running = True

while running:
    if randomnumber == guess:
        print("Good Job! You guessed it")
        running = False
        break
    elif randomnumber < guess:
        print("Too high")
    elif randomnumber > guess:
        print("Too low")
    guess = int(input("Try again: "))
