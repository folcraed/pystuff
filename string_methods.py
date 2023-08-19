"""This is a lesson in string manipulation."""

# If we wanted to output a multiline sentence, it
# could be done like this:

message = """Bobby's World was a good
cartoon in the 1990's."""

print(message)

# We can also use indexes to get parts of a string
print(message[8:13])

# We can use the method "count" to see how often
# something appears in the string
print(message.count('o'))
print(message.count('cartoon'))

# To find the starting index of a string (and if
# it exists) use the 'find' method. If it doesn't
# exist, Python will return a -1
print(message.find('house'))

# While the 'replace' method will replace one text string with
# another, it doesn't do it in-place. In order to get the replacement,
# you would need to assign it to a new variable.

message.replace('World', 'Universe')  # Doesn't work
print(message)

new_message = message.replace('World', 'Universe')  # Works
print(new_message)

# You can also do a re-assignment of the string to make it work,
# though this permanently changes the original string.
message = message.replace('World', 'Universe')  # Works
print(message)

another_message = message.replace('Universe', 'Planet')
print(another_message)

# To get an idea of what methods are available for a
# string variable, you can use the 'dir' function.
# print(dir(message))

# You can also get more information on what methods are available,
# and on individual methods with the 'help' function.
# print(help(str))  # Will list all the string methods
print(help(str.find))  # will show the find method info.
