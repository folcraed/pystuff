"""
This was an interesting exercise. The idea is if the math() module did not
exist in Python, there was no min() or max() functions, how would one find
which number was the smallest, largest and middle in a series of 3 numbers?
It's an example of passing variables between functions, and calling one
function from another.
"""

num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101


def smallest_of_two(n1, n2):
    if n1 < n2:
        return n1
    return n2


def largest_of_two(n1, n2):
    if n1 > n2:
        return n1
    return n2


def remove_one_of_three(n1, n2, n3, remove):
    if n1 == remove:
        return n2, n3
    elif n2 == remove:
        return n1, n3
    return n1, n3


def remove_one_of_two(n1, n2, remove):
    if n1 == remove:
        return n2
    return n1


def remove_two_of_three(n1, n2, n3, remove1, remove2):
    n1, n2 = remove_one_of_three(n1, n2, n3, remove1)
    return remove_one_of_two(n1, n2, remove2)


def smallest(n1, n2, n3):
    return smallest_of_two(smallest_of_two(n1, n2), n3)


def largest(n1, n2, n3):
    return largest_of_two(largest_of_two(n1, n2), n3)


def middle(n1, n2, n3):
    return remove_two_of_three(n1, n2, n3, smallest(n1, n2, n3), largest(n1, n2, n3))


print(
    f"Sum of smallest = {smallest(num11, num12, num13) + smallest(num21, num22, num23)}"
)
print(f"Sum of middle = {middle(num11, num12, num13) + middle(num21, num22, num23)}")
print(f"Sum of largest = {largest(num11, num12, num13) + largest(num21, num22, num23)}")
