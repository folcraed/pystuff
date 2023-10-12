"""
Asks for the user to enter the first names of their friends, and adds them
to a list. When the user has finished adding the names they want, they just
press ENTER. The list of names is then sorted alphabetically, then printed
back, all on one line, separated by commas.
"""

# Start with an empty list.
namelist = []

# Get the names from the user, add them to the list.
while True:
    name = input("Enter a friend's first name, <ENTER> to exit: ")
    if name == "":
        break
    namelist.append(name)

# Sort the list of name alphabetically.
namelist.sort()

# Return the sorted list all on one line.
print("Your sorted list of friends is: ", end="")
for item in namelist:
    if item == namelist[-1]:
        print(item, end=".")  # If the last in the list, end the line.
        break
    print(f"{item},", end=" ")  # Print the name separated with a comma and space.

print()
