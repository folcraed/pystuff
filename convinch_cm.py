"""
This takes a measurement from the user, in either inches
or centimeters and converts it to the other measure.
"""

conv_which = input("Convert to 'c' centimeters or 'i' inches? ")


if conv_which == "i":
    centimeters = int(input("How many centimeters? "))
    converted = centimeters * 0.39370
    print(f"{centimeters} centimeters equal {converted:.1f} inches")
elif conv_which == "c":
    inches = int(input("Hom many inches? "))
    converted = inches / 0.39370
    print(f"{inches} inches equal {converted:.1f} centimeters")
else:
    print("Can't convert that!")
