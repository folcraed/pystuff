"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""


from pcinput import get_string
from math import sqrt

user_input = get_string("Enter a floating point number: ")

x = user_input.find(".")


def getFraction(val):
    """Takes the user supplied number string and returns the decimal part."""
    result = ""
    for i in range(x + 1, len(val)):
        result += val[i]
    return result


decimals = getFraction(user_input)
print(f"The fractional numbers are {decimals}.")
squareroot = sqrt(int(decimals))
print(f"That number's square root is {squareroot:.2f}.")
