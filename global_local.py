#
# In this example, we define a variable, and it would appear
# to be global, but it isn't. We can iterate, or call it,
# but not much else

x = 6


def example():
    print(x)
    z = 5  # z, however, is a local variable
    print(z)


example()  # This works, we can output z here.
# print(z)  # But this will not, we can't outside it's function


# Another exanple is:
def example2():
    print(x)  # This will work
    print(x + 5)  # So will this


# x += 6  # but this won't, even though x appears global.
# We can use the variable, inside the function, but we
# can't modify it there.
example2()


# If we want to modify x in our function, we have
# to declare it a global within the function
def example3():
    global x
    print(x)
    x += 5
    print(x)  # Now it will work


example3()


# But if we don't want our global variable modified in a local function
# we can instead assign a new variable to hold the original value, and
# use that instead
def example4():
    globx = x
    print(globx)
    globx += 5
    print(globx)


example4()


# Another way to handle this, though not as easily understandable
# is to bring the variable into the function. Then if we wish we can
# pass the modified version back to the original variable. This is
# known as 'shadowing' and in some linters can cause a weak error.
def example5(x):
    print(x)
    x += 7
    print(x)
    return x


x = example5(x)
print(x)
