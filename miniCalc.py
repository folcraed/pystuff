# Creating a mini calculator using string input

num1, oper, num2 = input("Enter calculation: ").split()

num1 = int(num1)
num2 = int(num2)

# Doing it this way will induce an error if the operator isn't a choice.
# if oper == "+":
#     result = num1 + num2
# elif oper == "-":
#     result = num1 - num2
# elif oper == "*":
#     result = num1 * num2
# elif oper == "/":
#     result = num1 / num2
# else:
#     This prints out, but...
#     print("Not a valid operator")
# So does this, which throws an error due to no operator.
# print("{} {} {} equals {}".format(num1, oper, num2, result))

if oper == "+":
    print("{} + {} = {}".format(num1, num2, (num1 + num2)))
elif oper == "-":
    print("{} - {} = {}".format(num1, num2, (num1 - num2)))
elif oper == "*":
    print("{} * {} = {}".format(num1, num2, (num1 * num2)))
elif oper == "/":
    print("{} / {} = {}".format(num1, num2, (num1 / num2)))
else:
    print("Use +, -, *, or / next time!")
