"""
A very simple tic-tac-toe game
"""

# Create the board and some default variables
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# By default, the game always starts with user "X
user = "X"

# Initialize row and column variables
r = 0
c = 0

# Since there are only 9 spaces in the game, set a limit
MAXMOVE = 9


def display_board(b):
    """Display the board using the 'board' variable, which gets
    modified as the game progresses."""
    print("  1 2 3")
    for row in range(3):
        print(row + 1, end=" ")
        for col in range(3):
            print(b[row][col], end=" ")
        print()


def get_row_column(row, col):
    """Gets the placement for the player's token, and places it on
    the board. If the player enters a space already taken, it gives
    a warning and lets them try again, using recursion."""
    placement = input("Enter the row and column you choose: ")
    row = int(placement[0]) - 1
    col = int(placement[-1]) - 1
    if board[row][col] != "-":
        print("Space already used, try again.")
        get_row_column(row, col)
    else:
        board[row][col] = user


def switch_player(player):
    """Switches between the two players."""
    if player == "X":
        player = "O"
        return player
    elif player == "O":
        player = "X"
        return player


def winner(b):
    """Checks the board to see if either player has won the game."""
    if b[0][0] != "-" and b[0][1] == b[0][0] and b[0][2] == b[0][0]:
        return True
    elif b[1][0] != "-" and b[1][1] == b[1][0] and b[1][2] == b[1][0]:
        return True
    elif b[2][0] != "-" and b[2][1] == b[2][0] and b[2][2] == b[2][0]:
        return True
    elif b[0][0] != "-" and b[1][0] == b[0][0] and b[2][0] == b[0][0]:
        return True
    elif b[0][1] != "-" and b[1][1] == b[0][1] and b[2][1] == b[0][1]:
        return True
    elif b[0][2] != "-" and b[1][2] == b[0][2] and b[2][2] == b[0][2]:
        return True
    elif b[0][0] != "-" and b[1][1] == b[0][0] and b[2][2] == b[0][0]:
        return True
    elif b[0][2] != "-" and b[1][1] == b[0][2] and b[2][0] == b[0][2]:
        return True
    else:
        return False


# Start the game
move = 0
while True:
    display_board(board)
    get_row_column(r, c)
    if winner(board) is True:
        display_board(board)
        print(f"Player {user} has won!")
        break
    move += 1
    if move == MAXMOVE:  # If all 9 spaces are taken, call the game a draw
        display_board(board)
        print("Sorry, it's a draw.")
        break
    user = switch_player(user)
