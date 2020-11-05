# This is a guess the number game.

import random 
myNumber = random.randint(1, 20)

print("Hello. What is your name?")
userName = input()

print("Well, " + str(userName) + ", I am thinking of a number between 1 and 20.")

try:
    for guessesTaken in range(1, 7):
        print("Take a guess.")
        guess = input()
        if int(guess) > myNumber:
            print("Your guess is too high")
        elif int(guess) < myNumber:
            print("Your guess is too low")
        else:
            break
except ValueError:
    print("You can\'t input decimal numbers.")

if guess == str(myNumber):
    print("Good job, " + userName + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(myNumber) + ".")
    
