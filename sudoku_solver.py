# General logic
# If a square has only one possible value => place value
# If a row, column or box has only one possible value => place value
# If neither are true then guess and check for errors

from more_itertools import grouper

# Set size of board
BOARD_SIZE = 9
BOX_SIZE = 3 

def get_board():
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


def print_board(bo):
    """
    Function to print the board - requires an iterable bo which is the board
    """
    for i, row in enumerate(bo):
        set = grouper(row, BOX_SIZE)
        print(*set, sep=' | ')

        if (i+1)%BOX_SIZE==0 and i+1>0:
            print('-'*33)


if __name__ == "__main__":
    print_board(get_board())
