"""
This is an example of creating and using 'first-class' functions.
It shows creating a function that can be used anywhere, something
similar I suppose to C header files. They're mainly closures, which
take a task and break it down into sub-tasks by using enclosed
functions within the main function.
"""


def square(x):
    return x * x


def cube(x):
    return x * x * x


# This my_map function takes in another function and its arguments.
# When called it executes the function, so the original function
# doesn't get executed until it's passed to my_map. When passing
# a function to my_map, it's done without () so it doesn't get executed
# until my_map does it.
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# We pass in the function we want executed to my_map with arguments.
squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(cubes)
print(squares)


# Another example is using a closure to do complex wrapping of text.
# Here it takes in two variables, the tag we want to use, and the text
# we want to wrap in the tags.
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


# We create a function 'print_h1' which is simply a copy of html_tag with
# a pre-defined tag, ready to have text wrapped in it.
print_h1 = html_tag('h1')

# Here we call our new function and supply the text we want wrapped.
print_h1('Test Headline!')
print_h1('Another Headline!')


# The same is done here, we create a function 'pre-loaded' using our
# first-class function 'html_tag' and then use it to wrap the text we want.
print_p = html_tag('p')
print_p('Test Paragraph!')
