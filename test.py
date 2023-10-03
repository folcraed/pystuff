"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""

from pcinput import get_integer

TOTAL = 10
low = 0
high = 0
div_three = 0

for x in range(TOTAL):
    num = get_integer("Please enter number " + str(x+1) + ": ")
    if x == 0:
        low = num
    if num < low:
        low = num
    if num > high:
        high = num
    if num % 3 == 0:
        div_three += 1

print(f"The lowest was {low}, the highest {high}, and {div_three} were divisable by 3.")
