"""
This is an attempt to do the interest rate calculation
that was done in the C++ program I did following Derek Banas
video tutorial. Just want to see if I know enough about Python.
"""

investment = float(input("How much to invest? "))
interest = float(input("What is the interest rate? "))

rate = interest * .01

for i in range(1, 11):
    investment = investment + investment * rate

print("Value after 10 years is : {:.2f}".format(investment))
