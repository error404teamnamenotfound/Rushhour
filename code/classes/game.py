import math
import random

from code.classes.board import Board


class Game():
    """
    Creates game object to play Rush Hour. Checks for possible moves,
    picks random move and checks for win.
    """
    def __init__(self, source_file):
        self.board = Board(source_file)
    
    def find_moves(self):
        """
        Creates list of possible moves.
        """

        # create new move list
        moves = []
        
        # loop over cars on board
        for car in self.board.cars:
            row = car.row
            col = car.col

            # check for empty spaces left and right from horizontal car
            if car.orientation == 'H':
                if self.board.layout[row][col - 1] == '_' and col != 0:
                    moves.append([car, 'l'])

                # prevent border error with try/except
                try:
                    if self.board.layout[row][col + car.length] == '_':
                        moves.append([car, 'r'])
                except IndexError:
                    pass

            # check for empty spaces up and down from vertical car
            if car.orientation == 'V':
                if self.board.layout[row - 1][col] == '_' and row != 0:
                    moves.append([car, 'u'])

                # prevent border error
                try:
                    if self.board.layout[row + car.length][col] == '_':
                        moves.append([car, 'd'])
                except IndexError:
                    pass

        print(moves)
        
        return moves

    def move(self):
        """
        Moves car based on random move from list of valid moves.
        """

        # create list of valid moves
        moves = self.find_moves()

        # get random move from possible moves
        choice = random.choice(moves)

        # move car based on direction; change coordinates of car
        if choice[1] == 'l':
            choice[0].col -= 1
        elif choice[1] == 'r':
            choice[0].col += 1
        elif choice[1] == 'u':
            choice[0].row -= 1
        elif choice[1] == 'd':
            choice[0].row += 1

    def win(self):
        """
        Returns true and prints success if red car (XX) is at exit.
        Example: 6x6 exit is at (3, 6) --> index [2][5].
        """

        # get column right of red car
        col_x = [car.col + 2 for car in self.board.cars if car.name == 'X'][0]

        # get coordinates of exit
        row_e = math.ceil(self.board.size / 2) - 1
        col_e = self.board.size - 1

        # check if X is on exit or the row towards exit is empty
        if self.board.layout[row_e][col_e] == 'X' or all(self.board.layout[row_e][col_x:] == '_'):
            print("success")
            return True

        return False
        