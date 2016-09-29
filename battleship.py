from random import randint

# Building the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Hiding the ship

ship_row = random_row(board)
ship_col = random_col(board)

# Game play for 5 turns
turn = 0
for turn in range(5):
    print("This is turn number " + str(turn + 1))
    guess_row = int(raw_input("Guess a row: ")) - 1
    guess_col = int(raw_input("Guess a column: ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            #TODO: Validate for NANs, empty strings, etc.
            print "You're officially off-map."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 4:
            print("Game Over!")
    turn += 1
