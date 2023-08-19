#!/usr/bin/python


# Converts to/from miles to kilometers

convert = input("Convert miles 'm' or kilometers 'k'?: ")
distance = float(input("Enter distance to convert: "))


def to_kilometers(distance):
    kilometers = distance * 1.60634
    print("{} miles equals {:.2f} kilometers".format(distance, kilometers))


def to_miles(distance):
    miles = distance * 0.62137
    print("{} kilometers equals {:.2f} miles".format(distance, miles))


if convert == 'm':
    to_kilometers(distance)
elif convert == 'k':
    to_miles(distance)
else:
    print("Must be either 'm' or 'k'!")
