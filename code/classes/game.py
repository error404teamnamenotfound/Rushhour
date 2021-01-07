from code.classes.board import Board
import random

class Game():
    def __init__(self, source_file):
        self.board = Board(source_file)
        self.board.draw_board()
    
    def find_moves(self):
        self.moves = []
        
        # loop over cars on board
        for car in self.board.cars:
            row = car.row
            col = car.col
            if car.orientation == "H":
                try:
                    if self.board.layout[row][col - 1] == "_" and col != 0:
                        self.moves.append([car, 'l'])
                except IndexError:
                    pass
                try:
                    if self.board.layout[row][col + car.length] == "_":
                        self.moves.append([car, 'r'])
                except IndexError:
                    pass
            if car.orientation == "V":
                try:
                    if self.board.layout[row - 1][col] == "_" and row != 0:
                        self.moves.append([car, 'u'])
                except IndexError:
                    pass
                try:
                    if self.board.layout[row + car.length][col] == "_":
                        self.moves.append([car, 'd'])
                except IndexError:
                    pass

        return self.moves

    def move(self):
        self.find_moves()

        # get random move from possible moves
        choice = random.choice(self.moves)

        # move car
        if choice[1] == 'l':
            choice[0].col -= 1
        elif choice[1] == 'r':
            choice[0].col += 1
        elif choice[1] == 'u':
            choice[0].row -= 1
        elif choice[1] == 'd':
            choice[0].row += 1
        
        print("succesful move")

    def win(self):
        if self.board.layout[2][5] == "X":
            print("success")
            return True
        return False
        