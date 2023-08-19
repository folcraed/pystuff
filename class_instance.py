#
# Part of object-oriented programming. Example
# of use of a class, and the class' instances.
#
# This defines the class. Though 'email' is not
# part of the original variables, it uses ones from
# the class, so it works.


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

# Create functions to return the class instances.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_rate(self):
        return '{}'.format(self.pay)

    def emp_email(self):
        return '{}'.format(self.email)


# Enter the instances
emp_1 = Employee('Rob', 'Boudreau', 50000)
emp_2 = Employee('Tess', 'Wilkinson', 60000)

# Get the class instances
print(Employee.fullname(emp_2))
print(Employee.pay_rate(emp_2))
print(Employee.emp_email(emp_2))
