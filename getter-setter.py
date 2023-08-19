#
# Changes the 'class_instance.py' lesson to make the Employee class
# update-able and changeable.
#


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
# I can remove this method and instead create a property decorator for it
#        self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

# I can do the same for the fullname method.
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# But if I want to change the Employee's full name, it's easier to
# do with a setter than to do each individually.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')  # This removes space between names
        self.first = first
        self.last = last

# We can also make an Employee deleter, to remove employees from the class
    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('', '')

# Now I can just type in a full name and it will be parsed into the class
emp_1.fullname = 'Corey Shafer'
emp_2.fullname = 'Tess Wilkinson'

# This is a lot more efficient than doing the below
# emp_1.first = 'Jim'
# emp_1.last = 'Jones'

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print(emp_2.first)
print(emp_2.fullname)
print(emp_2.email)
del emp_2.fullname
print('Employee 1 is: ' + emp_1.fullname)
print('Employee 2 is: ' + emp_2.fullname)
