import csv
from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid

class MiniBFS():
    """
    Creates mini Breadth First algorithm that tries to find a shorter path of moves
    through a moves set in steps of given step size.
    """
    def __init__(self, sourcefile, step_size, moves_set, max_moves):
        self.game = Game(sourcefile)
        self.sourcefile = sourcefile
        self.step_size = step_size
        self.moves_set = moves_set
        self.max_moves = max_moves
        self.final_moves_set = []

    def get_mini_moves_set(self):
        """
        Returns part of moves set and removes that from original moves set.
        """

        # get part of moves set of length step size if possible
        if len(self.moves_set) >= self.step_size:
            old_moves_set = self.moves_set[:self.step_size]
            del self.moves_set[:self.step_size]

        # otherwise get remaining part of moves set
        else:
            self.step_size = len(self.moves_set)
            old_moves_set = self.moves_set[:]
            self.moves_set.clear()

        return old_moves_set

    def try_moves(self, old_moves_set):
        """
        Moves cars from moves set to find the goal layout for the mini Breadth First.
        """
        for choice in old_moves_set:
            self.game.move(choice)
        self.game.board.create_layout()

    def run_breadthfirst(self):
        """
        Runs small Breadth First algorithm to find shorter path from starting moves
        to goal layout. Returns path and way of winning.
        """

        # get goal layout
        layout = self.game.board.layout

        # run breadth first hybrid version
        bfs = BFHybrid(self.sourcefile, layout, self.final_moves_set, self.max_moves)
        new_moves_set = bfs.run()

        # check kind of win
        won = bfs.won_game()

        return new_moves_set, won

    def run(self):

        while self.moves_set:
            
            # print length of moves set to keep track
            print(len(self.moves_set))
            
            # get small part of moves set
            old_moves_set = self.get_mini_moves_set()

            # move moves to goal layout
            self.try_moves(old_moves_set)
            
            # run breadth first hybrid version
            new_moves_set, won = self.run_breadthfirst()

            # show in terminal what kind of win was reached
            print(f"won: {won}")

            # if full game was won, add to final moves set and stop
            if won == 1:
                self.final_moves_set = self.final_moves_set + new_moves_set
                return self.final_moves_set

            # if shorter moves set found, add to self.moves_set and start over
            elif won == 2:
                self.final_moves_set = self.final_moves_set + new_moves_set

            # if max steps was reached, keep old set of moves
            elif won == 3:
                self.final_moves_set = self.final_moves_set + old_moves_set

        return self.final_moves_set
