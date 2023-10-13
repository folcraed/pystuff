"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""


def display_board(b):
    print("  1 2 3")
    for row in range(3):
        print(row + 1, end=" ")
        for col in range(3):
            print(b[row][col], end=" ")
        print()


board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
board[1][1] = "X"
board[0][2] = "0"
display_board(board)
