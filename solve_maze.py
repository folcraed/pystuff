"""
This uses the 'pc_maze.py' file as a module, which creates a maze with 16
'blocks'. This then shows two ways of using recursion to find the exit to
the maze. The first one, 'leads_to_exit()', outputs all the steps taken
in finding the route through the maze. The second one, 'find_the_exit()',
only outputs the path it took to find the way out.

The purpose of this exercise is to show using recursion in functions. It's
not something that should be done often, but can have some advantages when
used properly.
"""


from pc_maze import entrance, exit, connected


def leads_to_exit(comingfrom, cell, depth):
    """
    This shows every step of the process of finding the correct
    path. It indents each search as it goes to make it clear where
    it has searched.
    """
    indent = depth * 4 * " "
    if cell == exit():
        return True
    for i in range(entrance(), exit() + 1):
        if i == comingfrom:
            continue
        if not connected(cell, i):
            continue
        print(f"{indent} Check connection {cell} -> {i}")
        if leads_to_exit(cell, i, depth + 1):
            print(f"{indent} Path found: {cell} -> {i}")
            return True
    return False


if leads_to_exit(0, entrance(), 0):
    print("Path found!")
else:
    print("Path not found")
print()


def find_the_exit(comingfrom, cell):
    """
    This shows the steps taken to find the exit as a list, it does
    not show all the steps, only the solution.
    """
    if cell == exit():
        return "{}".format(exit())
    for i in range(entrance(), exit() + 1):
        if i == comingfrom:
            continue
        if not connected(cell, i):
            continue
        check = find_the_exit(cell, i)
        if check != "":
            return "{} -> {}".format(cell, check)
    return ""


check = find_the_exit(0, entrance())
if check != "":
    print(f"Path found! {check}")
else:
    print("Path not found")
