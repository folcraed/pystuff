"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""

num = 9

# This starts the first row of the table
print(". |", end="")

# This adds the number of entries to the first row,
# making sure they each occupy 3 character places
# to keep the rows even as the numbers increase.
for i in range(1, num + 1):
    print("{:>3}".format(i), end="")
print()

# This prints a divider. Knowing that each number in our
# table occupies three character spaces, we make sure the
# divider will fit all.
for i in range(3 * (num + 1)):
    print("-", end="")
print()

# This prints out the rest of the table, incrementing as
# we move down the rows.
for i in range(1, num + 1):
    print(i, "|", end="")
    for j in range(1, num + 1):
        print("{:>3}".format(i * j), end="")
    print()
