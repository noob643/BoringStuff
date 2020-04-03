# Test Case Dictionary
from collections import Counter
import string
import sys
current_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# Function
def isValidChessBoard(pieces):
# Dictionary with valid chess pieces and their number
    chess_pieces = {"wpawn" : 8,
                    "bpawn" : 8,
                    "wknight" : 2,
                    "bknight" : 2,
                    "wbishop" : 2,
                    "bbishop" : 2,
                    "wrook" : 2,
                    "brook" : 2,
                    "wqueen" : 1,
                    "bqueen" : 1,
                    "wking" : 1,
                    "bking" : 1}

    # Check pieces are in valid squares
    #Create a list of all possible board positions
    squares = []
    board_numbers = list(range(1,9))
    board_letters = list(string.ascii_lowercase[0:8])
    for z in board_numbers:
        for y in board_numbers:
            p = str(board_numbers[z-1])+str(board_letters[y-1])
            squares.append(p)
    
    # Check all pieces positions are valid
    condition = all(elem in squares for elem in pieces.keys())
    if condition == False:
        sys.exit("ERROR: Some pieces are not in valid positions!")
    
    # Check pawns are in valid squares
    for z in squares[:8]:
        try:
            condition = pieces[z] == "wpawn"
            if condition == True:
                sys.exit("ERROR: White pawn in Row 1!")
        except KeyError:
            continue
    for z in squares[-8:]:
        try:
            condition = pieces[z] == "bpawn"
            if condition == True:
                sys.exit("ERROR: Black pawn in Row 8!")
        except KeyError:
            continue
    
    # Check all pieces are valid and do not exceed max number
    pieces_on_board = Counter(list(pieces.values()))
    all(elem in chess_pieces.keys() for elem in pieces_on_board.keys())
    for z in pieces_on_board.keys():
        condition = chess_pieces[z]>=pieces_on_board[z]
        if condition == False:
            sys.exit("ERROR: Quantity of some pieces is exceeded!")
            
    # Check one king on the board
    condition = pieces_on_board["bking"]==1 and pieces_on_board["wking"]==1
    if condition == False:
        sys.exit("ERROR: King(s) Missing!")
        
    print ("Chessboard is Valid!")  
    
isValidChessBoard(current_board)
