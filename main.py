import time

from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game


if __name__ == '__main__':

    # create new game
    test = Game('data/Rushhour12x12_7.csv')

    # keep track of moves
    moves = 0

    # draw first board
    test.board.draw_board()

    # keep track of time
    t0 = time.perf_counter()

    # make random moves until win
    while not test.win():
        test.move()
        test.board.create_layout()
        #test.board.draw_board()
        moves += 1
        #time.sleep(0.1)

    test.board.draw_board()
    # stop time
    t1 = time.perf_counter() - t0

    # print number of played moves, time elapsed and speed
    print(f"{moves} in {t1:.2f} s")
    print(f"{moves/t1:.1f} moves/s")

