# Converts to/from square feet to acres

print()
convert = input("Enter letter matching what you want to convert, square feet 'f' or acres 'a'?: ")
distance = float(input("Enter distance to convert: "))
print()


def to_acres(sq_feet):
    acres = sq_feet / 43560
    print("{:.0f} square feet equals {:.2f} acres".format(sq_feet, acres))


def to_square_feet(acres):
    sq_feet = acres * 43560
    print("{} acres equals {:.0f} square feet".format(acres, sq_feet))


if convert == 'f':
    to_acres(distance)
elif convert == 'a':
    to_square_feet(distance)
else:
    print("Must be either 'a' or 'f'!")
