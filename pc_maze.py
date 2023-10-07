"""
This creates a simple maze which connects some numbered cells. You can find
the entrance by calling the function 'entrance()', the exit given by the 
function 'exit()'. The module also has the function 'connected()' that takes
two arguments, returning True if there is a direct connection between cells,
and False if not. The entrance is always the lowest number, the exit highest.
"""


def connected(x, y):
    if x > y:
        return connected(y, x)
    if (x, y) in (
        (1, 5),
        (2, 3),
        (3, 7),
        (4, 8),
        (5, 6),
        (5, 9),
        (6, 7),
        (8, 12),
        (9, 10),
        (9, 13),
        (10, 11),
        (10, 14),
        (11, 12),
        (11, 15),
        (15, 16),
    ):
        return True
    return False


def entrance():
    return 1


def exit():
    return 16
