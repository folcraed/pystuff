# Takes a solve-for-x problem from the user and solves it.


# First we need to get the problem from the user
def get_problem():
    """Prompts the user for their formula to solve
    and checks to see if it's properly formatted."""
    query = input("Enter the formula to solve, or 'q' to quit: ")
    if query.find("q") != -1:
        exit()
    elif query.find(" ") != -1:
        print("You must not use spaces in the formula, try again!")
        get_problem()
    elif query.find("x") == -1:
        print("You must use 'x' as missing element, try again!")
        get_problem()
    return query


# We place the user's query in a global variable for processing
problem = get_problem()

# We create some placeholders for later use, so we don't get an error
end_of = len(problem)
last_place = end_of - 1
op_pos = 0
num1 = 0
num2 = 0


# These functions will do the math once we've processed the user's input
def addup(first, second):
    """Adds the numbers together to solve for 'x'."""
    x_is = float(first) + float(second)
    print("x equals {:.1f}".format(x_is))


def subup(first, second):
    """Subtracts one number from the other to solve for 'x'."""
    x_is = float(first) - float(second)
    print("x equals {:.1f}".format(x_is))


def divup(first, second):
    """Divides one number by the other to solve for 'x'."""
    x_is = float(first) / float(second)
    print("x equals {:.1f}".format(x_is))


def multup(first, second):
    """Multiplys the numbers together to solve for 'x'."""
    x_is = float(first) * float(second)
    print("x equals {:.1f}".format(x_is))


# We need to find out where 'x', the operator and '=' are
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
    num1 = problem[(op_pos + 1) : equals]


if x_loc != last_place:
    num2 = problem[(equals + 1) : end_of]
else:
    num2 = problem[(op_pos + 1) : equals]

# We've broken the input string into 4 positions, 2 containing the
# known numbers, one for "x" and one for the "=" sign.
# Knowing where x is, we use one of the marker positions, 0, 2 or 4.
# This position lets us know what is 'x' and what are numbers.
if x_loc == last_place:
    x_loc = 4
elif x_loc == 0:
    x_loc = 0
else:
    x_loc = 2

# Finally, using our marker positions, we create the logic to evaluate x
if (operator == "+" and x_loc == 0) or (operator == "+" and x_loc == 2):
    subup(num2, num1)
elif operator == "+" and x_loc == 4:
    addup(num1, num2)
elif operator == "-" and x_loc == 0:
    addup(num2, num1)
elif (operator == "-" and x_loc == 2) or (operator == "-" and x_loc == 4):
    subup(num1, num2)
elif (operator == "*" and x_loc == 0) or (operator == "*" and x_loc == 2):
    divup(num2, num1)
elif operator == "*" and x_loc == 4:
    multup(num1, num2)
elif operator == "/" and x_loc == 0:
    multup(num2, num1)
elif (operator == "/" and x_loc == 2) or (operator == "/" and x_loc == 4):
    divup(num1, num2)
else:
    print("Uh oh... Something went wrong!")
