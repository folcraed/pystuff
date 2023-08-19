"""
Exercise in creating a class and using class methods to work with variable
data. The exercise uses class methods, decorators and variables. The end
result should be a program that can take user input and present the data
in useful ways.
"""


class Employee:
    raise_amount = 1.04  # Class variable instead of instance variable.
    num_of_employed = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employed += 1

    # Here we create a method to return a human-readable string.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Here we use the class variable, which must start with the class instance.
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Using a class method with decorator to modify a variable. This will allow
    # us to change the variable outside of the class definition itself.
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Using a class method to parse employee information to aid input.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(', ')
        return cls(first, last, int(pay))


# This is an example of a subclass, using inheritance.
class Developer(Employee):
    def __init__(self, first, last, pay, program_lang):
        super().__init__(first, last, pay)
        self.program_lang = program_lang

# When adding a field to the original class, we need to create a new method for it.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, program_lang = emp_str.split(', ')
        return cls(first, last, int(pay), program_lang)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# These are added directly to the class, showing how tedious it can be this way
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Linus', 'Torvalds', 120000)
dev_1 = Developer('Ikey', 'Doherty', 95000, 'C')
dev_2 = Developer('Dave', 'Edmundson', 90000, 'C++')
mgr_1 = Manager('Sue', 'Smith', 110000)


# This will use the 'from_string' subclass method to make adding easier.
new_dev = input("Enter a new employee, Last, First, Salary: ")
employee_new = Developer.from_string(new_dev)
mgr_1.add_employee(employee_new)


print(mgr_1.email)
mgr_1.add_employee(emp_1)
mgr_1.add_employee(emp_2)
mgr_1.add_employee(dev_1)
mgr_1.add_employee(dev_2)
mgr_1.print_employees()
