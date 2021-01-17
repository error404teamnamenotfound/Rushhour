import random

class Randomise():
    """ random algorithm """

    def __init__(self):
    
    def run(self):
            
        # initialize best moves list
        best_moves = [None] * 100000

        # play game untill interrupted with ctrl-c
        try:
            while True:
                # create new game
                game = Game('data/Rushhour12x12_7.csv')

                # draw first board
                # draw_board(game.board.layout)
                # matrix = [[ord(char) for char in row] for row in game.board.layout]

                # matplotlib.rcParams['backend'] = 'TkAgg'
                # print(matplotlib.rcParams['backend'])

                # print(matrix)

                # #fig = plt.figure()
                # plt.matshow(matrix)
                # plt.show()

                # keep track of time
                t0 = time.perf_counter()

                last_move = [None, 0]

                # make random moves until win
                while not game.win() and len(game.moves) <= len(best_moves):

                    # find possible moves
                    moves_list = game.find_moves(last_move)

                    # use random algorithm to choose moves
                    choice = random_move(moves_list)

                    last_move = choice
                    # move car and create new layout
                    game.move(choice)
                    game.board.create_layout()

                    # # add move to list of moves (if latest move is same, just add 1 to move)
                    # if moves and [choice[0].name, choice[1]] == moves[-1]:
                    #     moves[-1][1] += choice[1]
                    # else:
                    #     moves.append([choice[0].name, choice[1]])

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

                # # write output
                # with open('output.csv', 'w', newline='') as outputfile:
                #     fieldnames = ['car', 'move']
                #     writer = csv.writer(outputfile)
                #     writer.writerow(fieldnames)
                #     writer.writerows(best_moves)

        except KeyboardInterrupt:

        # write output
            with open('output.csv', 'w', newline='') as outputfile:
                fieldnames = ['car', 'move']
                writer = csv.writer(outputfile)
                writer.writerow(fieldnames)
                writer.writerows(best_moves)


    def random_move(moves_list):
    
        return random.choice(moves_list)


    