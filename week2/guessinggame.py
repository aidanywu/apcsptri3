 
import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("Pick a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("Good job, you guessed the number!")
        break
    else:
        print("Incorrect, try again.")