# This was interesting, I'd never seen this math style used before.
# Saw it on a video, had to try it out.
# In order to cube a number without using the math library functions,
# you can double up the * sign and it will work.


def cubed_num(num):
    return num**3


num = int(input('Enter a number to cube: '))

print('Your number cubed is ' + str(cubed_num(num)))
