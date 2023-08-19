#
# This asks for a number, then outputs the
# pythagorian algorythm for that number. It's
# something like Fibonacci numbers.

# The input fuction will not work in Sublime's output window.
from math import sqrt
n = input("Maximum Number? ")
n = int(n) + 1
for a in range(1, n):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c_square - c**2) == 0:
            print(a, b, c)
