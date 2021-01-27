from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid

class MiniBFS():
    """
    Creates mini Breadth First algorithm that tries to find a shorter path of moves
    through a moves set in steps of given step size.
    """
    def __init__(self, sourcefile, step_size, moves_set, max_moves):

        # initialize final moves set
        self.final_moves_set = []

        # set variables
        self.sourcefile = sourcefile
        self.step_size = step_size
        self.moves_set = moves_set
        self.max_moves = max_moves

    def get_goal_layout(self, goal_moves):
        """
        Creates new game to set moves for the goal layout.
        """
        game = Game(self.sourcefile)
        for choice in tuple(goal_moves):
            game.move(choice)
        game.board.create_layout()

        return game.board.layout

    def get_starting_moves(self):
        """
        Returns starting moves for breadth first.
        """
        return self.final_moves_set

    def get_goal_moves(self):
        """
        Returns moves set that is needed to create a goal
        for the breadth first.
        """
        if len(self.moves_set) >= self.step_size:
            old_set = self.moves_set[:self.step_size]
            del self.moves_set[:self.step_size]
        else:
            self.step_size = len(self.moves_set)
            old_set = self.moves_set[:]
            self.moves_set.clear()

        goal_moves = self.final_moves_set + old_set
        return goal_moves

    def run_breadthfirst(self, layout, starting_moves):
        """
        Runs small Breadth First algorithm to find shorter path from starting moves
        to goal layout. Returns path and way of winning.
        """

        # run breadth first hybrid version
        bfs = BFHybrid(self.sourcefile, layout, starting_moves, self.max_moves)
        new_moves_set = bfs.run()

        # check kind of win
        won = bfs.won_game()

        return new_moves_set, won

    def run(self):
        """
        Runs mini breadth first algorithm.
        """
        while self.moves_set:
            print(len(self.moves_set))

            # get starting moves
            starting_moves = self.get_starting_moves()

            # get goal moves
            goal_moves = self.get_goal_moves()

            # get goal layout
            layout = self.get_goal_layout(goal_moves)

            # run breadthfirst
            new_moves_set, won = self.run_breadthfirst(layout, starting_moves)

            print(f"won: {won}")

            #if full game was won, add to final moves set and stop
            if won == 1:
                self.final_moves_set += new_moves_set
                return self.final_moves_set

            # if shorter moves set found, add to self.moves_set and start over
            elif won == 2:
                self.moves_set = new_moves_set + self.moves_set

            # if max steps was reached, keep old set of moves
            elif won == 3:
                self.final_moves_set = goal_moves

        return self.final_moves_set
