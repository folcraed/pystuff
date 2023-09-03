from pcinput import get_integer, get_string, get_float

num1 = get_integer("Please enter an interger: ")
new_prompt = get_string("Please enter a new prompt for a floating point number: ")
num2 = get_float(new_prompt)

print("The sum of", num1, "times", num2, "is {:.2f}".format(num1 * num2))
