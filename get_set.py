# This exercise is showing how to use setters and getters to make working
# with classes easier.


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Originally we had the line below to create an email address.
    # The problem with that is, if we decide to change one of the names,
    # it wouldn't be used, the email setter below is part of the class,
    # so it would default to the original name.
    #         self.email = first + '.' + last + '@company.com'

    # The solution is to create a method to make an email for us. The added
    # advantage is: any code written to work with the old way will still work.
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # This setter below makes entering employees easier. Instead of having to
    # having a name like the 1st example below, placing the name in parenthesis
    # we can enter it just as a straight string, as the second example below.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('John', 'Smith')

print(emp_1.fullname)

emp_1.first = 'Jim'

print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = 'Ikey Doherty'

print(emp_1.fullname)
print(emp_1.email)
