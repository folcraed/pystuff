'''
The object of this is going to be taking a formula input from a user,
and converting it to a usable form for processing. We'll be looking
for "x", finding where it is in the formula, then parsing the rest
to solve for it.

Currently it uses spaces to delimit items, I'd eventually like to find
a way to parse the items (numbers vs. operators) without the need for them.

UPDATE: We did that in "algebra_problem.py", see it.
'''

# First we get the problem to solve from the user.
solve = input("Enter formula to solve: ")


# Then we check to make sure they entered if properly.
count = solve.count(" ")
if count < 4:
    print("You must use spaces in formula!")
    exit()
elif solve.find("x") == -1:
    print("You must use 'x' as the missing parameter!")
    exit()


# To iterate over it, we convert it to a list of values.
def ConvertToList(string):
    sequence = list(string.split(" "))
    return sequence


ConvertedFormula = ConvertToList(solve)


# Next we find where in the formula 'x' is.
SolveFor = ConvertedFormula.index("x")


# We create some math functions to do the work of solving.
def addNums(val1, val2):
    return val1 + val2


def subNums(val1, val2):
    return val1 - val2


def multiNums(val1, val2):
    return val1 * val2


def divNums(val1, val2):
    return val1 / val2


# Knowing where 'x' is, we assign the remaining numbers.
if SolveFor == 0:
    num1 = int(ConvertedFormula[2])
    num2 = int(ConvertedFormula[4])
elif SolveFor == 2:
    num1 = int(ConvertedFormula[0])
    num2 = int(ConvertedFormula[4])
else:
    num1 = int(ConvertedFormula[0])
    num2 = int(ConvertedFormula[2])


# Depending on where x was and what operation was required,
# we process the formula to produce a result for 'x'.
if ConvertedFormula[1] == "+" and SolveFor == 0:
    print("The value of x is: " + str(subNums(num2, num1)))
elif ConvertedFormula[1] == "+" and SolveFor == 2:
    print("The value of x is: " + str(subNums(num2, num1)))
elif ConvertedFormula[1] == "+" and SolveFor == 4:
    print("The value of x is: " + str(addNums(num1, num2)))
elif ConvertedFormula[1] == "-" and SolveFor == 0:
    print("The value of x is: " + str(addNums(num2, num1)))
elif ConvertedFormula[1] == "-" and SolveFor == 2:
    print("The value of x is: " + str(subNums(num1, num2)))
elif ConvertedFormula[1] == "-" and SolveFor == 4:
    print("The value of x is: " + str(subNums(num1, num2)))
elif ConvertedFormula[1] == "*" and SolveFor == 0:
    print("The value of x is: " + str(divNums(num2, num1)))
elif ConvertedFormula[1] == "*" and SolveFor == 2:
    print("The value of x is: " + str(divNums(num2, num1)))
elif ConvertedFormula[1] == "*" and SolveFor == 4:
    print("The value of x is: " + str(multiNums(num1, num2)))
elif ConvertedFormula[1] == "/" and SolveFor == 0:
    print("The value of x is: " + str(multiNums(num2, num1)))
elif ConvertedFormula[1] == "/" and SolveFor == 2:
    print("The value of x is: " + str(divNums(num1, num2)))
elif ConvertedFormula[1] == "/" and SolveFor == 4:
    print("The value of x is: " + str(divNums(num1, num2)))
else:
    print("You must have entered something wrong!")
