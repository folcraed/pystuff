#
# Sorting list, tuples and objects with various functions and methods.
#

from operator import attrgetter  # This will be used later in exercise.

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

print('The original list:\t', li)

s_li = sorted(li)
# Using the function sorts the original list into a
# new variable but doesn't affect the original list.

print('Sorted List:\t', s_li)

li.sort()
# Using a method would sort the original list, changing it.
# This might not be what's wanted. It produces the same result
# as above with less code, but the original list is changed.
print('Sorted Original List:\t', li)
print()

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)

# Tuples can't use the method, the code will fail if
# tried. Tuples are immutable, so the method would fail,
# producing an error.
print('Sorted Tuple:\t', s_tup)
print()

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)

# When sorting a dictionary, using the function as above will only
# return the dictionary keys
print('Sorted Dict Keys:\t', s_di)
print()

# The method "items()" will return a tuple of all the items in a dictionary.
list_of = di.items()
print("Dictionary items: ", list_of)

# The method "values()" returns a tuple of just the values from the dictionary.
print("Values of items: ", di.values())

# Working with classes is a bit harder, to sort keys in a class
# we have to create a function based on our keys.


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('William', 37, 7000)
e2 = Employee('Sarah', 29, 8000)
e3 = Employee('Grey Jack', 43, 9000)

# To sort the employees, we need to create a list of them
employees = [e1, e2, e3]


# Here's where we create a function to do the sorting.
# Without the function, Python won't know how to sort
# the list. You can see the error if you comment out
# the function and remove the key from the print variable.
def e_sort(emp):
    return emp.name


# You can change the sort function return value by any in the list.
# In this example it could be emp.name, emp.age or emp.salary.
s_employees = sorted(employees, key=e_sort)

# You can also reverse the sort using the usual 'reverse=True' method.
r_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees)
print()
print(r_employees)
print()

# We can eliminate the function if desire and just use a lambda instead
l_employees = sorted(employees, key=lambda e: e.name)

print(l_employees)
print()

# Another way is using the operator function from the standard library
ag_employees = sorted(employees, key=attrgetter('age'))

print(ag_employees)
