"""This will show the different ways to concatenate."""


greeting = 'Hello'
name = 'Michael'

# This way is okay, but can become cumbersome.
# Especially when you have a lot of variables.
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Often in more complex cases it's better to use placeholders
# and the string 'format' method.
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
