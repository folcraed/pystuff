# Various methods of working with loops and iterations

nums = [1, 2, 3, 4, 5]

# This is a very simple loop that prints the contents of nums
for num in nums:
    print(num)

# Another way to iterate is using the 'range' function
# If we don't want it to start at the default 0, we have
# to implicitly tell the range where to start. And remember,
# it will end at the last value, but not print it.
for i in range(1, 6):
    print(i)

# If we need our loop to stop when a certain condition is met, use 'break'
for num in nums:
    if num == 4:
        print('I found 4!')
        break
    print(num)

# If we want to catch when a condition is met, but otherwise continue
# the loop, use 'continue'
for num in nums:
    if num == 4:
        print('I found 4!')
        continue
    print(num)

# Another way to loop through a series of values is with 'while'
x = 0
while x < 10:
    print(x)
    x += 1

# To stop a while loop at when something happens, use a 'break' statement
# Note you can't use 'continue' in a while loop, when it reaches the
# condition, it will stop regardless and the rest will never run.
# If a condition with continue is needed, us a for loop.
y = 1
while y < 11:
    if y == 5:
        print('I found 5!')
        break
    print(y)
    y += 1
