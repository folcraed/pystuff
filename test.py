"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""

from pcinput import get_integer

total = 0
count = 0
entry = 1
while entry != 0:
    prompt = get_integer("Please enter a number, 0 to exit: ")
    if prompt == 0:
        print("The total is", total, "and the average is", total / count)
        exit()
    count += 1
    total += prompt
