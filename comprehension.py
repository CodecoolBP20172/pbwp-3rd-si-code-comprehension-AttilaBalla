# This program generates a random number between 1 and 20 then prompts the user to try guessing which number it is.
# It is always possible to nail the number using binary search

import random  # imports external module for random generation

guessesTaken = 0

print('Hello! What is your name?')
myName = input()  # asks the user to input its name

number = random.randint(1, 20)  # generates the random number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:  # while loop rolls until either the user nails the number or fails 6 times
    print('Take a guess.')
    guess = input()
    guess = int(guess)  # converts the input to Int - will crash if the user enters anything but numbers

    guessesTaken += 1  # incremention

    if guess < number:   # self explanatory
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break  # breaks out of the loop if this condition is met

if guess == number:
    guessesTaken = str(guessesTaken)  # type conversion, print needs this in str format
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:  # this only triggers after the while loop IF the user did not guess the number
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
