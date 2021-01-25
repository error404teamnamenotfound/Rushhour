from code.algorithms.randomise import Randomise
from code.algorithms.loopremover import LoopRemover
from code.algorithms.minibfs import MiniBFS

class Hybrid3():
    def __init__(self, sourcefile):
        self.sourcefile = sourcefile

    def run(self):
        # run randomise untill less than 100
        randomise = Randomise(self.sourcefile)
        moves_set = randomise.run()

        # run loopremover
        loopremover = LoopRemover(self.sourcefile, moves_set)
        moves_set = loopremover.run()

        # run minibfs in steps of 10
        minibfs = MiniBFS(self.sourcefile, 10, moves_set)
        moves_set = minibfs.run()

        return moves_set


        # run hybrid2 in steps of 10 from beginning (bfs can do max 4/5 steps) to find the earliest win

        # while still getting shorter
            # run hybrid2 from beginning(/end?) in steps of 6
            # run hybrid2 from beginning(/end?) in steps of 7
        # stop if both 6 and 7 don't make move set shorter

        # return move set


        """
        Maybe add loopcutters in between while loop.
        Add possibility to ctrl-c so it will still be returned if it takes to long.
        """
