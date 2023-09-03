prompt = "Enter 'c' for Celsius to Fahrenheit, 'f' for Fahrenheit to Celsius: "
convert = input(prompt)


if convert == "c":
    temp = int(input("Enter temperature to convert: "))
    converted = (temp * 9 / 5) + 32
    print(f"{temp} degrees Celsius equals {converted:.1f} Fahrenheit")
elif convert == "f":
    temp = int(input("Enter temperature to convert: "))
    converted = ((5 / 9) * (temp - 32))
    print(f"{temp} degrees Fahrenheit equals {converted:.1f} Celsius")
else:
    print("Can't convert that!")
