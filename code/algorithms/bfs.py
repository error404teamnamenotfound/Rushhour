from code.classes.game import Game
import numpy as np
import copy

class BreadthFirst():
    def __init__(self, sourcefile):
        self.game = Game(sourcefile)
        self.archive = {} # keep track of all visited nodes
        last_move = [None, 0]
        self.queue = [[move] for move in self.game.find_moves(last_move)]
        #self.queue = [[['A', -2], ['B', -2], ['C', -1], ['D', -1], ['G', -2], ['H', -1], ['F', 2], ['X', -1], ['K', -2], ['I', -3], ['L', -3], ['K', 2], ['F', -1], ['H', 3], ['X', 3]]]
        #self.queue = [[['A', -1], ['C', -1], ['G', -2], ['L', -2], ['J', -3], ['I', 2], ['H', 1], ['E', 3], ['D', -1], ['H', -1], ['I', -3], ['H', 1], ['E', -2], ['J', 3], ['E', 2], ['L', 2], ['X', 3]]] # all the valid moves of one layer
        #self.queue = [[['A', -1], ['B', 1], ['G', 1], ['E', 1], ['A', -1], ['G', -1], ['E', -1], ['G', 1], ['M', 1], ['K', 1], ['G', 1], ['F', -1], ['J', -1], ['O', -1], ['S', -1], ['M', 1], ['K', -1], ['B', 1], ['O', 1], ['J', 1], ['F', -1], ['K', -1], ['G', -1], ['M', -1], ['R', 1], ['B', -1], ['E', -1], ['K', 1], ['G', -1], ['R', -1], ['M', 1], ['T', 1], ['S', 1], ['S', -2], ['G', -1], ['T', -1], ['S', -1], ['G', 1], ['T', 1], ['G', -1], ['M', 1], ['D', -1], ['T', -1], ['U', -1], ['D', 1], ['S', 1], ['M', -1], ['C', -2], ['H', -1], ['M', 1], ['S', -1], ['M', 1], ['K', 1], ['S', 1], ['C', -1], ['S', -1], ['D', 1], ['H', -1], ['D', 2], ['C', 1], ['G', 1], ['E', 1], ['I', -1], ['H', 1], ['S', 1], ['G', 1], ['D', -1], ['H', -1], ['C', -1], ['I', 1], ['D', -1], ['H', 1], ['G', 1], ['I', -1], ['S', 1], ['F', 1], ['A', 1], ['H', 1], ['B', -1], ['I', -1], ['G', 1], ['H', -2], ['S', 2], ['G', -1], ['I', 2], ['D', 1], ['I', -1], ['B', 1], ['S', -2], ['A', 1], ['G', -1], ['H', -1], ['G', 1], ['I', 1], ['E', -1], ['R', -1], ['B', -1], ['O', 1], ['J', 1], ['C', 1], ['T', -1], ['T', -1], ['P', -1], ['I', 1], ['T', 1], ['M', -1], ['P', -1], ['I', 1], ['M', 1], ['P', 1], ['S', 1], ['B', 1], ['P', -1], ['A', 1], ['T', -1], ['P', -1], ['C', -1], ['X', -1], ['N', -1], ['E', 1], ['C', -1], ['N', -1], ['A', -1], ['U', -1], ['C', 1], ['N', 1], ['P', -1], ['Q', -1], ['P', 2], ['R', -1], ['M', -1], ['A', 1], ['M', 1], ['Q', -1], ['M', -1], ['A', -1], ['C', 1], ['R', 1], ['N', -1], ['X', 1], ['Q', -1], ['A', 1], ['M', 1], ['P', 1], ['A', -1], ['S', 2], ['K', -1], ['U', -1], ['A', 1], ['R', -1], ['U', 1], ['C', -1], ['K', 1], ['O', 1], ['L', -1], ['X', 1], ['I', 1], ['B', 1], ['I', 1], ['J', 1], ['B', -1], ['T', 1], ['M', -1], ['I', -1], ['T', 1], ['A', -1], ['X', -1], ['P', -1], ['E', -1], ['T', -1], ['B', 1], ['A', -1], ['E', 1], ['B', 1], ['E', 1], ['X', 1], ['N', 1], ['X', -1], ['M', -1], ['K', -1], ['P', 1], ['N', -1], ['K', 1], ['B', -1], ['J', -1], ['I', 1], ['B', 1], ['O', -1], ['A', 1], ['C', -1], ['O', 1], ['M', 1], ['I', -1], ['D', 1], ['E', -1], ['F', 1], ['D', 2], ['I', -1], ['Q', -1], ['L', 1], ['A', -1], ['D', 1], ['F', -1], ['C', 1], ['L', -1], ['F', 1], ['J', 1], ['X', 6]]]

    def get_moves_set(self):
        """
        Returns first item in queue.
        """
        return self.queue.pop(0)

    def try_moves(self):
        """
        Moves cars according to set of moves and creates new layout.
        """
        pass

    def add_to_queue(self, moves_set):
        """
        Finds new moves and adds to queue.
        """

        # find new possible moves
        new_moves = self.game.find_moves(moves_set[-1])

        # add new moves series to queue
        for new_move in new_moves:
            self.queue.append(moves_set + [new_move])

    def run(self):

        while True:
        #for i in range(20):

            if len(self.queue) % 1000 == 0:
                print(len(self.queue[0]))

            # get first move from queue
            moves_set = self.get_moves_set()

            #print(moves_set)

            # try moves
            for choice in moves_set:
                #print(choice)
                self.game.move(choice)

            # create new layout
            self.game.board.create_layout()
            #self.game.board.draw_board()
            
            # check for win
            if self.game.win():
                
                print("we won")
                self.game.board.draw_board()

                # return winning set of moves
                return moves_set

            # continue if layout is not in archive
            if self.game.board.layout.tobytes() not in self.archive:

                self.archive[self.game.board.layout.tobytes()] = self.game.board.layout
                
                self.add_to_queue(moves_set)

            # if not any(np.array_equal(self.game.board.layout, old) for old in self.archive):

            #     # save layout in archive
            #     self.archive.append(self.game.board.layout)

            #     # add new moves sets to queue
            #     self.add_to_queue(moves_set)
            # first go back to original layout
            moves_set.reverse()

            for choice in moves_set:
                self.game.move([choice[0], -choice[1]])

            

