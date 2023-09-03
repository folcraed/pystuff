'''
This breaks an original numerical amount into it's
equivalent in money, producing how many dollars,
quarters, dimes, nickels and pennies would be needed
to equal the original amount.
'''

amount = 1268  # Set the original amount

dollars = int(amount / 100)  # Calculate how many of each are in the amount.
remainder = (amount % 100)  # Calculate the left over change

# For each value, find if it's singular or plural, and set which
# for later printing.
val1 = ""
if dollars > 1:
    val1 = "Dollars,"
else:
    val1 = "Dollar,"

quarters = int(remainder / 25)
remainder = (remainder % 25)
val2 = ""
if quarters > 1:
    val2 = "Quarters,"
else:
    val2 = "Quarter,"

dimes = int(remainder / 10)
remainder = (remainder % 10)
val3 = ""
if dimes > 1:
    val3 = "Dimes,"
else:
    val3 = "Dime,"

nickels = int(remainder / 5)
val4 = "Nickel,"  # Since 2 nickels is a dime, we'll naver have more than one

pennies = (remainder % 5)
val5 = ""
if pennies > 1:
    val5 = "Pennies"
else:
    val5 = "Penny"

print()
print("The original amount of", amount, "equals:\n")
print(dollars, val1, quarters, val2, dimes, val3, nickels, val4,
      "and", pennies, val5)
