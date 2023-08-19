# This shows the various string arrays and how they're used.
# First is lists, which are contained in square brackets []

courses = ['History', 'Math', 'Physics', 'CompSci', 'Biology']

# This will print out all the strings in the list
print(courses)

# This will show how many strings are in our list.
print(len(courses))

# Just like in string indexes, you can return a list value by it's index.
print(courses[3])
print(courses[:4])

# To add something to the list, use the 'append' method
courses.append('Art')
print(courses)

# To add something in a specific index, use the 'insert' method
courses.insert(2, 'Psych')
print(courses)

# You can add another list to the list...
courses_2 = ['Art', 'Education']
# courses.insert(0, courses_2)
# print(courses)

# That's often not what we want, as it adds the entire list to a single index
# It's generally better to use the 'extend' method, to add just the values of
# the list to the original one
courses.extend(courses_2)
print(courses)

# You can remove items with the 'remove' method, but usually you want to do
# something with them. The 'pop' method may be better for this.
popped = courses.pop(6)
print(popped)
print(courses)

# If we want to reverse the order of the list, we use the 'reverse' method
# courses.reverse()
# print(courses)
#
# If we want to sort the list, use the 'sort' method
# courses.sort()
# print(courses)

# If we want a sorted list without affecting the original list order, use the
# 'sorted' function.
sorted_courses = sorted(courses)
print(sorted_courses)  # The sorted version
print(courses)  # Showing the original isn't changed

# To find something in a list, use the 'index' method with a search string
print(courses.index('CompSci'))

# To find if something exists in the list, use the 'in' keyword
print('Math' in courses)

# If we want to get a printout list of our list items, we can create a function
# The 'start=1' in the function tells it to start at 1 instead of 0
for index, course in enumerate(courses, start=1):
    print(index, course)

# We can also print a more 'human readable' list using the 'split' method
course_str = ' - '.join(courses)
print(course_str)
