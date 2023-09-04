"""
Calculates the length of the diagonal side of a triangle from
the length of it's perpendicular sides.
"""

from pcinput import get_float
from math import sqrt

side1 = get_float("Enter the length of the first side: ")
side2 = get_float("Enter the length of the second side: ")

# The calculation adds the squares of the two sides together
# then calculates the square root of the addition.
side3 = sqrt(side1**2 + side2**2)

print()
print("The length of the diagonal is {:.2f}.".format(side3))
