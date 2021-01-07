from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

if __name__ == '__main__':
    test = Game('data/Rushhour9x9_4.csv')
    moves = 0
    while not test.win():
        test.move()
        test.board.create_layout()
        test.board.draw_board()
        moves += 1
    print(moves)

