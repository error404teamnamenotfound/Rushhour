import random
import csv
import time

from code.classes.game import Game

class Randomise():
    """
    Algorithm to solve a Rush Hour board with random moves.
    """

    def __init__(self, sourcefile):
        
        # get board file
        self.sourcefile = sourcefile

        # initialize best moves list
        self.best_moves = [None] * 10000
    
    def run(self):
        """
        Plays games untill interrupted with ctrl-c.
        """
        counter = 0
        try:
            while True:
                # keep track of time
                t0 = time.perf_counter()

                # play game
                moves_set = self.play_game()

                # stop time
                t1 = time.perf_counter() - t0

                # print number of played moves, time elapsed and speed
                if counter % 1000 == 0:
                    print(f"{len(moves_set)} in {t1:.2f} s")
                #print(f"{len(moves_set)/t1:.1f} moves/s")

                counter += 1

                # update best moves list when new list is smaller
                if len(moves_set) < len(self.best_moves):
                    self.best_moves = moves_set
            
        except KeyboardInterrupt:

            # return best moves list
            return self.best_moves

    def random_move(self, valid_moves):
        """
        Returns a random move from a list of valid moves.
        """
        return random.choice(valid_moves)

    def new_game(self):
        """
        Creates a new Game object.
        """
        return Game(self.sourcefile)

    def play_game(self):
        """
        Plays one game of Rushhour with random moves.
        """
        # initialize game, moves list and last move
        game = self.new_game()
        moves_set = []
        last_move = [None, 0]

        # make random moves until win
        while not game.win() and len(moves_set) <= len(self.best_moves):

            # find possible moves
            valid_moves = game.find_moves(last_move)

            # if no moves possible, run again without last move
            if not valid_moves:
                valid_moves = game.find_moves([None, 0])

            # use random algorithm to choose moves
            choice = self.random_move(valid_moves)

            # move car and create new layout
            game.move(choice)
            game.board.create_layout()

            # append choice to moves list and save as last_move
            moves_set.append(choice)
            last_move = choice
        
        #game.board.draw_board()
        
        return moves_set



    
