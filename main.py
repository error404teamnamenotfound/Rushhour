import csv
import time

from code.algorithms.random import random_move
from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game


if __name__ == '__main__':

    # initialize list for moves
    # try:
    #     with open('output.csv', 'r') as outputfile:
    #         next(outputfile)
    #         best_moves = outputfile.readlines()
    # except FileNotFoundError:
    
    # QUICK FIX, TODO
    best_moves = [["_"] for i in range(10000)]

    # play game untill interrupted with ctrl-c
    try:
        while True:
            # create new game
            game = Game('data/Rushhour6x6_2.csv')

            # keep track of moves
            moves = []

            # draw first board
            game.board.draw_board()

            # keep track of time
            t0 = time.perf_counter()

            # make random moves until win
            while not game.win() and len(moves) <= len(best_moves):
                moves_list = game.find_moves()
                choice = random_move(moves_list)
                choice[0].move(choice[1])
                game.board.create_layout()
                #game.board.draw_board()

                # add move to list of moves
                if moves and [choice[0].name, choice[1]] == moves[-1]:
                    moves[-1][1] += choice[1]
                else:
                    moves.append([choice[0].name, choice[1]])
                
                #time.sleep(0.1)

            # draw final board
            game.board.draw_board()

            # stop time
            t1 = time.perf_counter() - t0

            # print number of played moves, time elapsed and speed
            print(f"{len(moves)} in {t1:.2f} s")
            print(f"{len(moves)/t1:.1f} moves/s")

            # make best_moves list at first try
            # if best_moves is None:
            #     best_moves = moves

            # update best moves list when new list is smaller
            if len(moves) < len(best_moves):
                best_moves = moves

    except KeyboardInterrupt:
        
        # write output
        # TODO board name in output file name
        with open('output.csv', 'w', newline='') as outputfile:
            fieldnames = ['car', 'move']
            writer = csv.writer(outputfile)
            writer.writerow(fieldnames)
            writer.writerows(best_moves)

