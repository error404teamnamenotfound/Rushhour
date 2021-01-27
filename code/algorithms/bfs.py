from code.classes.game import Game
import numpy as np

class BreadthFirst():
    """
    Creates Breadth First algorithm to solve a Rush Hour board.
    """
    def __init__(self, sourcefile):
        self.game = Game(sourcefile)
        self.archive = {}

        # initialize first "last move"
        last_move = [None, 0]

        # put first possible moves in queue
        self.queue = [[move] for move in self.game.find_moves(last_move)]
                
    def get_moves_set(self):
        """
        Returns first item in queue.
        """
        return self.queue.pop(0)

    def try_moves(self, moves_set):
        """
        Moves cars according to set of moves and creates new layout.
        """
        for choice in tuple(moves_set):
            self.game.move(choice)
        self.game.board.create_layout()

    def won_game(self):
        if self.game.win():
            self.game.board.draw_board()
            return True
        return False

    def not_in_archive(self):
        """
        Checks if layout is already in archive. If not, adds layout to archive.
        """
        if self.game.board.layout.tobytes() not in self.archive:
            self.archive[self.game.board.layout.tobytes()] = self.game.board.layout.tobytes()
            return True
        return False

    def add_to_queue(self, moves_set):
        """
        Finds new moves and adds to queue.
        """
        new_moves = self.game.find_moves(moves_set[-1])
        for new_move in tuple(new_moves):
            self.queue.append(moves_set + [new_move])

    def reverse_moves(self, moves_set):
        """
        Reverses moves that are made to get back to beginning board.
        """
        moves_set.reverse()
        for choice in tuple(moves_set):
            self.game.move([choice[0], -choice[1]])

    def run(self):
        """
        Runs the Breadth First algorithm untill win or empty queue.
        Gets moves set from queue, moves those cars, checks for win,
        checks with archive and adds moves sets to queue.
        """

        # keep track of counter
        counter = 0

        while self.queue:

            # print depth of tree every 10000 steps
            if counter % 10000 == 0:
                print(len(self.queue[0]))

            # get first moves set from queue
            moves_set = self.get_moves_set()

            # move all moves from set
            self.try_moves(moves_set)

            # continue branch (add to queue) if layout is not in archive
            if self.not_in_archive():
                self.add_to_queue(moves_set)
            
            # check for win
            if self.won_game():

                # return winning set of moves
                return moves_set
            
            # reverse moves to original layout
            self.reverse_moves(moves_set)
            
            # add to counter
            counter += 1