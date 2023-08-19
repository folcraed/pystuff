# Takes a solve-for-x problem from the user and solves it.

# First we need to get the problem from the user
problem = input("Enter the formula to solve: ")

# We create some placeholders for later use, so we don't get an error
end_of = len(problem)
last_place = end_of - 1
op_pos = 0
num1 = 0
num2 = 0

# Then we need to make sure they entered a valid problem
if problem.find(" ") != -1:
    print("You must not use spaces in the formula, try again!")
    exit()
elif problem.find("x") == -1:
    print("You must use 'x' as missing element, try again!")
    exit()

# Next we need to find out where x, operator and = are
# First we look for x, and store it's location
x_loc = problem.find("x")

# Then we look for the operator, store it AND it's location
if problem.find("+") != -1:
    operator = "+"
    op_pos = problem.find("+")
elif problem.find("-") != -1:
    operator = "-"
    op_pos = problem.find("-")
elif problem.find("/") != -1:
    operator = "/"
    op_pos = problem.find("/")
else:
    operator = "*"
    op_pos = problem.find("*")


# Then we look for =, and store it's location
equals = problem.find("=")

# Using what we know, we pull out the existing numbers and store them
if x_loc != 0:
    num1 = problem[0:op_pos]
else:
    num1 = problem[(op_pos + 1):equals]


if x_loc != last_place:
    num2 = problem[(equals + 1):end_of]
else:
    num2 = problem[(op_pos + 1):equals]

# knowing where x is, we turn that into a marker position, 0, 2 or 4
# This simplifies the later function logic on which to use and how.
if x_loc == last_place:
    x_loc = 4
elif x_loc == 0:
    x_loc = 0
else:
    x_loc = 2


# We create functions to actually do the math
def addup(first, second):
    x_is = float(first) + float(second)
    print("x equals {:.1f}".format(x_is))


def subup(first, second):
    x_is = float(first) - float(second)
    print("x equals {:.1f}".format(x_is))


def divup(first, second):
    x_is = float(first) / float(second)
    print("x equals {:.1f}".format(x_is))


def multup(first, second):
    x_is = float(first) * float(second)
    print("x equals {:.1f}".format(x_is))


# Finally, using our marker position, we create the logic to evaluate x
if (operator == "+" and x_loc == 0) or (operator == "+" and x_loc == 2):
    subup(num2, num1)
elif (operator == "+" and x_loc == 4):
    addup(num1, num2)
elif (operator == "-" and x_loc == 0):
    addup(num2, num1)
elif (operator == "-" and x_loc == 2) or (operator == "-" and x_loc == 4):
    subup(num1, num2)
elif (operator == "*" and x_loc == 0) or (operator == "*" and x_loc == 2):
    divup(num2, num1)
elif (operator == "*" and x_loc == 4):
    multup(num1, num2)
elif (operator == "/" and x_loc == 0):
    multup(num2, num1)
elif (operator == "/" and x_loc == 2) or (operator == "/" and x_loc == 4):
    divup(num1, num2)
else:
    print("Something went wrong!")
