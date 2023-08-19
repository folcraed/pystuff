# Works with the my_module file to show importing

import os
from my_module import find_index, test
# If the module wasn't in the same path as the script we were running,
# we could append the path to where it is with the following:
# sys.path.append('<path_to_python_module>')

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')
print(index)
print(test)
# This shows how to use some of the standard library functions:
# print(sys.path)

# More on standard library functions, and some uses for them:
current_path = os.getcwd()
print(current_path)

am_here = current_path.find('python')
if am_here == -1:
    print("We're lost!")
else:
    print('We found python!')

print('All is well in the world!')
