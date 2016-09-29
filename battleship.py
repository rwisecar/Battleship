from random import randint
# Building the board

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Hiding the ship

ship_row = random_row(board)
ship_col = random_col(board)

# Allowing for user guesses
