# This will do a simple printout


def hello_func():
    print('Hello Function!')


hello_func()


# We can also use a return value and do things like print with it.
def hello_again():
    return 'Hello Again!'


print(hello_again())


# We can use methods with functions to make them do more
print(hello_again().upper())


# We can make functions take parameters and return them modified by it.
def greet_us(greeting):
    return '{} Human!'.format(greeting)


print(greet_us('Hi'))


# We can specify defaults to use with our functions
def custom_greet(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


# If we don't add a argument to the function it will use the defaults
print(custom_greet('Hi'))


# But if we pass an argument, it will use that instead
print(custom_greet('Hi', 'Rob'))


# Functions can take more than just single arguments, they can also take
# lists, tuples, sets and dictionaries.
# The following example takes a tuple and a dictionary as arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
# And here the variables are passed in when the function is called
# student_info('Math', 'Art', name='John', age=22)


# We can supply variables to our function...
courses = ['Math', 'Art']
info = {'name': 'John', 'age': '22'}


student_info(courses, info)


# That may not give us what we expected. If we change the function call...
student_info(*courses, **info)
