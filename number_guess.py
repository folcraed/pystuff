"""
This is a twist on the number guessing game. In this version, the user thinks
of a number, and the computer tries to guess it. There is a trap. If the user
tries to cheat and keep telling the computer the number is higher or lower, and
it runs out of guesses (high == low), it prints that number out and exits.
"""

from random import randint
from sys import exit

# Think of a number, and get the computer to guess it
# Start by setting lower and upper limits and a count
lower = 1
upper = 100
count = 0
correct = ""

# Tell the computer to pick a number between the lower and upper limits
while True:
    if lower == upper:  # Give a way out if lower and upper match
        print(f"The number must be {lower}, there's no more numbers left!")
        exit()
    guess = (randint(lower, upper))
    print(guess)
    correct = input("Was that right? ")
    count += 1
    if correct == "l":
        upper = guess - 1  # Reduce the upper limit by 1 so not guessed again
    elif correct == "h":
        lower = guess + 1  # Increase the lower limit by 1 so not guessed again
    else:
        break  # If guessed, any letter besides l or h will end the game

print(f"I guessed it, the number has to be {guess}, it took {count} guesses.")
