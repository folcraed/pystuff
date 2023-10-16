"""
The traditional game of Battleships.
"""
from pcinput import get_string
from random import randint

EMPTY = "."
BATTLESHIP = "X"
SHIPS = 3
WIDTH = 4
HEIGHT = 3
SUNK = "X"


def displayBoard(b):
    """Creates a visual grid for the playing board, labeling the rows and columns
    that the player can use for coordinates (such as "A1, D3, etc.") to target
    their strikes. It is called to update as the player enters each attempt.
    """
    print("  ", end="")
    for col in range(WIDTH):
        print(chr(ord("A") + col), end=" ")
    print()
    for row in range(HEIGHT):
        print(row + 1, end=" ")
        for col in range(WIDTH):
            print(b[row][col], end=" ")
        print()


def placeBattleships(h):
    """Places ships in random locations on the board. Checks to see if the location
    is already occupied by a ship, if so tries again. Repeats placing ships on the
    board until it reaches the maximum number of ships dictated in the variable.
    """
    for i in range(SHIPS):
        while True:
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            if h[y][x] == BATTLESHIP:
                continue
            if x > 0 and h[y][x - 1] == BATTLESHIP:
                continue
            if x < WIDTH - 1 and h[y][x + 1] == BATTLESHIP:
                continue
            if y > 0 and h[y - 1][x] == BATTLESHIP:
                continue
            if y < HEIGHT - 1 and h[y + 1][x] == BATTLESHIP:
                continue
            break
        h[y][x] = BATTLESHIP


def getTarget():
    """Displays a prompt to the player asking for which cell coordinate they
    wish to target. If the cell they enter is out of the grid range, it shows
    a warning, then gives them another chance to enter the correct grid.
    """
    while True:
        cell = get_string("Which cell do you want to shoot? ").upper()
        if len(cell) != 2:
            print("Please enter cell as XY,", "where X is a letter, and Y is a digit")
            continue
        if cell[0] not in "ABCD":
            print(
                "The first character of the cell",
                "should be a letter in the range A-" + chr(ord("A") + WIDTH - 1),
            )
            continue
        if cell[1] not in "123":
            print(
                "The second character of the cell should be",
                "a digit in the range 1-" + str(HEIGHT),
            )
            continue
        return ord(cell[0]) - ord("A"), ord(cell[1]) - ord("1")


# We create two separate lists, board and hidden.
board = []
for i in range(HEIGHT):
    row = WIDTH * [EMPTY]
    board.append(row)

# They have to be created separately, otherwise they are mirrored.
hidden = []
for i in range(HEIGHT):
    row = WIDTH * [EMPTY]
    hidden.append(row)


# We display the populated board created by the displayBoard function
displayBoard(board)
# We place the battleships on the hidden board, which is not displayed
placeBattleships(hidden)

hits = 0
moves = 0
while hits < SHIPS:
    x, y = getTarget()
    if hidden[y][x] == BATTLESHIP:
        # We look to see if the hit matches the hidden battleship list
        print("You sunk my battleship!")
        board[y][x] = SUNK  # If hit, place sunk marker in board list
        hits += 1
    else:
        print("Missed!")
        board[y][x] = "*"
        # If missed, mark the board list to show that cell has already been tried
    moves += 1
    displayBoard(board)  # Show the current state of play.

print(f"You needed {moves} moves to sink all battleships.")
