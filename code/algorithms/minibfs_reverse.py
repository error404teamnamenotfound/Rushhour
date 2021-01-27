from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid
from code.algorithms.minibfs import MiniBFS


class MiniBFS_reverse(MiniBFS):
    """
    Creates mini Breadth First algorithm that tries to find a shorter path of moves
    by going backwards through a moves set in steps of given step size.
    Inherits functions from forward mini bfs.
    """

    def get_starting_moves(self):
        """
        Removes old set of moves from self.moves_set. Self.moves_set functions
        as starting moves. The old set is returned so it can be added to final moves set if needed.
        """
        if len(self.moves_set) >= self.step_size:
            old_set = self.moves_set[-self.step_size:]
            del self.moves_set[-self.step_size:]
        else:
            self.step_size = len(self.moves_set)
            old_set = self.moves_set[:]
            self.moves_set.clear()

        return old_set
        
    def run(self):
        """
        Runs reversed mini breadth first algorithm.
        """

        while self.moves_set:
            print(len(self.moves_set))

            # get goal layout
            layout = self.get_goal_layout(self.moves_set)

            # get starting moves
            old_set = self.get_starting_moves()

            # run breadthfirst
            new_moves_set, won = self.run_breadthfirst(layout, self.moves_set)

            print(f"won: {won}")

            # if new moves set is shorter, run bfs from there
            if len(new_moves_set) < self.step_size and won != 3:
                self.moves_set += new_moves_set

            # if full game was won, new set is final moves
            elif won == 1:
                self.final_moves_set = new_moves_set
            
            # if no shorter move set was found, keep old set of moves
            else:
                self.final_moves_set = old_set + self.final_moves_set

        return self.final_moves_set
