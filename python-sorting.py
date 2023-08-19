from operator import attrgetter


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


# This custom function gives us a key to sort output of employees.
# Without it, the sort function wouldn't know the order wanted
# and fail with an error.
def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort)

# We could also use a lambda function on the fly.
l_employees = sorted(employees, key=lambda e: e.salary)

# Or we can use an imported Python method to get the key.
a_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)
print(l_employees)
print(a_employees)
