# Starting point for accessing the database

print("Welcome to the company database!")
print()
print("Choose one option, anything else will exit the program.")
choices = input(
    "What would you like to do, (a) add employee to data, (s) search data?: "
)
print()


if choices == "a":
    with open("addtodb.py") as f:
        exec(f.read())
if choices == "s":
    with open("searchdb.py") as f:
        exec(f.read())
else:
    print("Thanks for stopping by!")
    exit(0)
