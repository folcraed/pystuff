"""
This takes two words the user enters and compares them to each other,
one character at a time, looking for matching characters. When a match
is found, it's stored in a variable. Each matching character is then
compared to see if it's already in the variable, if it is, it's ignored.
When all the characters in the first word have been processed, the
resultant matching characters are printed out.
"""

# Get two words from the user and store them in variables
from pcinput import get_string

word1 = get_string("Enter the first word: ")
word2 = get_string("Enter the second word: ")

# create a third empty variable to hold matching characters
common = ""

# compare the first letter in the first word to the second word, one letter at a time
# if the letters match, compare it to letters in the third variable
# if the letters don't match the third variable, store the letter in the third variable
# when done, print the third variable
for letter in word1:
    if (letter in word2) and (letter not in common):
        common += letter
if common == "":
    print("The words have no characters in common.")
else:
    print(f"The words have '{common}' letters in common.")
