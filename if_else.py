# If, elif, else are used to check for true or false, and do something
# if one or the other is correct, if something is either true or false.
# It works with booleans.
# Things it can test for are:
#   Equals:                 ==
#   Not equal:              !=
#   Greater than:           >
#   Less than               <
#   Greater than or equal:  >=
#   Less than or equal      <=
#   Object identity:        is  <-- does it occupy the same memory?
#   and                     test for two or more values to be true
#   or                      test for one or the other value to be true
#   not                     test for the value to be false

language = 'Python'

if language == 'Python':
    print('Condition was true!')

# We can have it do something else if the condition proves false
new_language = 'Java'

if new_language == 'Python':
    print('Language is Python')
else:
    print('No match!')

# elif will add a check for another match, and can be used multiple times
next_language = 'Java'

if next_language == 'Python':
    print('Language is Python')
elif next_language == 'Java':
    print('Language is Java')
else:
    print('No match!')

# Here we use 'and' to test for mulitple values to be true
logged_in = True
user = 'Admin'

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Here we use 'or' to test if at least one value is true
logged_in = False
user = 'Admin'

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Use 'not' to see if something is already false, and returns true if it is.
if not logged_in:
    print('Please log in')
else:
    print('Welcome!')

# Object identity sees if two values are actually the same one, in other words
# if they refer to the same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Will show they hold the same values
print(a is b)  # Will check if they're the same object in memory

# We can prove the two variables hold different memory locations with 'id'
print(id(a))
print(id(b))

# The above proved false, and we can see in the output they're different
# When a variable IS based on another, they hold the same memory
x = [1, 2, 3]
y = x
print(x == y)  # Will show they hold the same values
print(x is y)  # Will check if they're the same object in memory
print(id(x))
print(id(y))  # Shows they hold the same memory location, they are the same.

# To test whether something is empty or not, we can use these functions
condition = 'Test'
next_condition = ''

if condition:
    print('Evaluated True')
else:
    print('Evaluated False')

if next_condition:
    print('Evaluated True')
else:
    print('Evaluated False')
