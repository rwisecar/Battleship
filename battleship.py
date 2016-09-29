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
'''For debugging:
print ("Row = " + str(ship_row))
print ("Column = " + str(ship_col))'''

# Allowing for user guesses

which_row = int(raw_input("Guess which row? ")) - 1
which_col = int(raw_input("Guess which column? ")) - 1

# Correct and Incorrect Guesses
if guess_row == ship_row and guess_col == ship_col:
    print("That's a hit! You sunk my battleship.")
else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)

turn = 1
for turn in range(5):
    print("This is turn number " + str(turn))
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        return
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 4:
                print("Game Over!")
        print_board(board)
    turn += 1
