"""
This takes a measurement from the user, in either meters
or feet and converts it to the other measure.
"""

conv_which = input("Convert from 'm' meters or 'f' feet? ")


if conv_which == "m":
    meters = int(input("How many meters? "))
    converted = meters * 3.2808
    print(f"{meters} meters equal {converted:.1f} feet")
elif conv_which == "f":
    feet = int(input("How many feet? "))
    converted = feet * 0.3048
    print(f"{feet} feet equal {converted:.1f} meters")
else:
    print("Can't convert that!")
