# Dictionaries store key-value pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

# To find the value of a key, access the key name
print(student['name'])

# If we try to access a key that doesn't exist, it will produce and error.
# To find if a key exists without creating an error, use the 'get' method
print(student.get('phone'))
print(student.get('phone', 'Not Found'))  # Creates a default error message

# If we want to add a key that doesn't exist yet, we can easily
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

# If we want to update the dictionary, we can just assign a new value to a key
student['name'] = 'Jane'
print(student)

# But if we want to update multiple keys, better to use the 'update' method
# and another dictionary. We can even add keys with this method on the fly
student.update({'name': 'Jean', 'age': 26, 'email': 'jean@compsci.edu'})
print(student)

# To get a list of dictionary items, use the 'items' method
print(student.items())

# To see key-item pairs, we can use a for loop
for key, value in student.items():
    print(key, value)
