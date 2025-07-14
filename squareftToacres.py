# Converts to/from square feet to acres

print()
convert = input(
    "Enter letter matching what you want to convert, square feet 'f' or acres 'a'?: "
)
distance = float(input("Enter distance to convert: "))
print()


def to_acres(sq_feet):
    """Takes a numeric input as number of square feet and divides it
    by the number of square feet in an acre, returning the acres."""
    acres = sq_feet / 43560
    print("{:.0f} square feet equals {:.2f} acres".format(sq_feet, acres))


def to_square_feet(acres):
    """Takes a numeric input as number of acres and multiplies it by
    the number of square feet in an acre, returning the square feet."""
    sq_feet = acres * 43560
    print("{} acres equals {:.0f} square feet".format(acres, sq_feet))


if convert == "f":
    to_acres(distance)
elif convert == "a":
    to_square_feet(distance)
else:
    print("Must be either 'a' or 'f'!")
