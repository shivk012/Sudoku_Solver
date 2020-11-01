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

    def __init__(self, value, row, col, block=None):
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
        self.block = block
    
    def __repr__(self):
        return f"Box, value is {self.value}, location is {self.row}, {self.column} \n"

    def reduce_possible(self, existing_vals: list):
        """
        Function to reduce the possible values by comparing against in input list and removing any matching values
        """
        self.possible = [pos_vals for pos_vals in self.possible if pos_vals not in existing_vals]

    def solve_value(self):
        """
        Function to set the value of the box if no other possible values remain
        """
        if len(self.possible)==1:
            self.value = self.possible[0]
            self.possible = []

class Block():
    """
    Class to represent a collection of boxes
    """
    
    def __init__(self, row, col, boxes=[]):
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
            # Add empty list for 2D List
            self.boxes.append([])
            # Add empty list into Block if new row of block
            if i%BOX_SIZE==0: self.blocks.append([])

            for j, val in enumerate(row):
                # Add Box to list of boxes - in 2D array format
                temp_box = Box(val, i, j)
                self.boxes[i].insert(j, temp_box)

                # Check if top left of a block
                block_row = int(i / BOX_SIZE)
                block_col = int(j/BOX_SIZE)
                if i%BOX_SIZE==0 and j%BOX_SIZE==0:
                    temp_block = Block(block_row, block_col)
                    self.blocks[block_row].insert(block_col, temp_block)
                else:
                    temp_block = self.blocks[block_row][block_col]

                temp_block.boxes.append(temp_box)
                temp_box.block=temp_block

    def __repr__(self):
        """
        Function to print out current block - needs to be converted to a string
        """
        out = ''
        for i, row in enumerate(self.board):
            set = grouper(row, BOX_SIZE)
            print(*set, sep=' | ')

            if (i+1)%BOX_SIZE==0 and i+1>0:
                print('-'*33)
    
    def row_check(self, row_n):
        """
        Function to check the row for errors (all unique values) and to set possible unique values for all boxes in the row.
        Will return:
            -1 for errors
            0 for no correct answers found
            1 for correct answers found
        """

        for box in self.boxes[row_n]:
            # Extract values in row
            row_vals = [box.value for box in self.boxes[row_n]]
            # Reduce possible values in the boxes
            for box in self.boxes[row_n]:
                box.reduce_possible(row_vals)
                box.solve_value()


    def col_check(self):
        """
        Function to check the column for errors (all unique values) and to set possible unique values for all boxes in the column.
        Will return:
            -1 for errors
            0 for no correct answers found
            1 for correct answers found
        """

        pass

    def block_check(self):
        """
        Function to check the block for errors (all unique values) and to set possible unique values for all boxes in the block.
        Will return:
            -1 for errors
            0 for no correct answers found
            1 for correct answers found
        """
        pass

    def testing(self):
        """
        Function for testing to print out various debugging info
        """
        self.__repr__()
        print('\n')
        self.row_check(1)
        self.__repr__()


if __name__ == "__main__":
    Sudoku = Board(get_board())
    Sudoku.testing()

