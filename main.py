import csv
import time

from code.algorithms.random import random_move
from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game


if __name__ == '__main__':
    
    # initialize best moves list
    best_moves = [None] * 100000

    # play game untill interrupted with ctrl-c
    try:
        while True:
            # create new game
            game = Game('data/Rushhour9x9_4.csv')

            # draw first board
            game.board.draw_board()

            # keep track of time
            t0 = time.perf_counter()

            # make random moves until win
            while not game.win() and len(game.moves) <= len(best_moves):

                # find possible moves
                valid_moves = game.find_moves()

                # use random algorithm to choose moves
                choice = random_move(valid_moves)

                # move car and create new layout
                game.move(choice)
                game.board.create_layout()
                
                #game.board.draw_board()
                #time.sleep(0.1)

            # draw final board
            game.board.draw_board()

            # stop time
            t1 = time.perf_counter() - t0

            # print number of played moves, time elapsed and speed
            print(f"{len(game.moves)} in {t1:.2f} s")
            print(f"{len(game.moves)/t1:.1f} moves/s")

            # update best moves list when new list is smaller
            if len(game.moves) < len(best_moves):
                best_moves = game.moves

    except KeyboardInterrupt:
        
        # write output
        with open('output.csv', 'w', newline='') as outputfile:
            fieldnames = ['car', 'move']
            writer = csv.writer(outputfile)
            writer.writerow(fieldnames)
            writer.writerows(best_moves)

