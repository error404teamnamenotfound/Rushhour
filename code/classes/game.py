import math, random

from code.classes.board import Board


class Game():
    """
    Creates game object to play Rush Hour. Checks for possible moves,
    picks random move and checks for win.
    """
    def __init__(self, source_file):
        self.board = Board(source_file)

    def find_moves(self, last_move):
        """
        Creates list of possible moves.
        """

        # create new move list
        valid_moves = []

        # loop over cars on board
        for car in tuple(self.board.cars.values()):

            if car.name == last_move[0]:
                continue

            row = car.row
            col = car.col

            # check for empty spaces left and right from horizontal car
            if car.orientation == 'H':
                for i in range(car.col):
                    if self.board.layout[row][col -1 - i] == '_' and col - i != 0:
                        valid_moves.append([car.name, -1 - i])
                    else:
                        break

                # prevent border error with try/except
                for i in range(self.board.size - car.length - car.col):
                    if self.board.layout[row][col + car.length + i] == '_' and col != self.board.size - 1:
                        valid_moves.append([car.name, 1 + i])
                    else:
                        break

            # check for empty spaces up and down from vertical car
            if car.orientation == 'V':
                for i in range(car.row):
                    if self.board.layout[row - 1 - i][col] == '_' and row - i != 0:
                        valid_moves.append([car.name, -1 - i])
                    else:
                        break
                
                # prevent border error with try/except
                for i in range(self.board.size - car.length - car.row):
                    if self.board.layout[row + car.length + i][col] == '_' and row != self.board.size - 1:
                        valid_moves.append([car.name, 1 + i])
                    else:
                        break
        
        return valid_moves

    def move(self, choice):

        car = self.board.cars[choice[0]]
        direction = choice[1]

        # set new coordinates for moved car
        if car.orientation == 'H':
            car.col += direction
        elif car.orientation == 'V':
            car.row += direction

    def win(self):
        """
        Returns true and prints success if red car (XX) is at exit.
        Example: 6x6 exit is at (3, 6) --> index [2][5].
        """

        # get coordinates of exit
        row_e = math.ceil(self.board.size / 2) - 1
        col_e = self.board.size - 1

        # check if X is on exit or the row towards exit is empty
        if self.board.layout[row_e][col_e] == 'X':

            return True
        return False
