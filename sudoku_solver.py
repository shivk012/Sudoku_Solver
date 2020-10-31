# General logic
# If a square has only one possible value => place value
# If a row, column or box has only one possible value => place value
# If neither are true then guess and check for errors

from more_itertools import grouper

# Set size of board
BOARD_SIZE = 9
BOX_SIZE = 3 

def get_board() -> list:
    """
    Function to provide a board for the rest of the functions
    """

    # Copied from wikipedia
    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    return board


class Box():
    """
    Class to represent each individual box
    """

    def __init__(self, value):
        # Value of the box
        self.value=value
        # Possible candidates for values
        if not value:
            self.possible=[1,2,3,4,5,6,7,8,9]
        else:
            self.possible=[]
        # Row of box
        self.row = -1
        # Column of box
        self.column = -1
        # Owning Block of box
        self.block = Block()

class Block():
    """
    Class to represent a collection of boxes
    """
    
    def __init__(self):
        # Row of Block (0-2 in the standard Sudoku board)
        self.row = -1
        # Row of Block (0-2 in the standard Sudoku board)
        self.column = -1
        # Collection of Boxes owned by this Block
        self.boxes = []


class Board():
    """
    Class that represents the entire board 
    """
    def __init__(self, game_board):
        self.board = game_board
        # Set up Box and Blocks
        
    def __repr__(self):
        """
        Function to print out current block
        """

        for i, row in enumerate(self.board):
            set = grouper(row, BOX_SIZE)
            print(*set, sep=' | ')

            if (i+1)%BOX_SIZE==0 and i+1>0:
                print('-'*33)

    

Sudoku = Board(get_board())

if __name__ == "__main__":

    Sudoku.__repr__()