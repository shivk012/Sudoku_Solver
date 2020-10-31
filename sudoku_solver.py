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

    def __init__(self, value, row, col):
        # Value of the box
        self.value=value
        # Possible candidates for values
        if not value:
            self.possible=[1,2,3,4,5,6,7,8,9]
        else:
            self.possible=[]
        # Row of box
        self.row = row
        # Column of box
        self.column = col
        # Owning Block of box
        self.block = None
    
    def __repr__(self):
        return f"Box, value is {self.value}, location is {self.row}, {self.column} \n"

class Block():
    """
    Class to represent a collection of boxes
    """
    
    def __init__(self, boxes, row, col):
        # Row of Block (0-2 in the standard Sudoku board)
        self.row = row
        # Row of Block (0-2 in the standard Sudoku board)
        self.column = col
        # Collection of Boxes owned by this Block
        self.boxes = boxes
    
    def __repr__(self):
        return f"Block, location is {self.row}, {self.column} \n"


class Board():
    """
    Class that represents the entire board 
    """
    def __init__(self, game_board):
        self.board = game_board
        # Set up Box and Blocks
        self.blocks = []
        self.boxes = []

        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                self.boxes.append(Box(col, i, j))

    def __repr__(self):
        """
        Function to print out current block - needs to be converted to a string
        """

        for i, row in enumerate(self.board):
            set = grouper(row, BOX_SIZE)
            print(*set, sep=' | ')

            if (i+1)%BOX_SIZE==0 and i+1>0:
                print('-'*33)
        
    def testing(self):
        """
        Function for testing to print out various debugging info
        """
        self.__repr__()
        print(self.boxes)
        print(self.blocks)

Sudoku = Board(get_board())

if __name__ == "__main__":
    Sudoku.testing()