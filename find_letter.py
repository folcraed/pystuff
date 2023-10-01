"""
This is an example of different ways to search strings for a letter. In this
example a tuple of words are given, then different ways of searching for a
particular letter in each word is shown.
"""

fruits = ("Cantelope", "Apple", "Pear", "Grape", "Cherry", "Orange", "Mango")

# This one looks for the letter "C" in the beginning of the word by string index.
for item in fruits:
    if item[0] == "C":
        print("This one starts with C:", end=" ")
    print(item)

# This one looks for the letter "C" by finding it in the first place in the string.
# If find() returns 0 (is true), it prints the comment plus the string.
for item in fruits:
    if item.find("C", 0) == 0:
        print("This one starts with C:", end=" ")
    print(item)

# This example searches when the location of the letter isn't known. If find()
# in not -1 (false), it prints the comment plus the string. Because find() returns
# the position if found, or -1 if not, we test for -1.
for item in fruits:
    if item.find("n") != -1:
        print("This one contains an n:", end=" ")
    print(item)
