from pcinput import get_integer
from sys import exit

num = get_integer("Please enter a positive integer: ")
if num < 0:
    print("You should have entered a positive integer!")
    exit()

print("Now I'm processing your integer '{}'".format(num))
print("Lots and lots of processing going on...")
print("Hundreds of lines of code here...")
