from code.algorithms.randomise import Randomise
from code.algorithms.loopremover import LoopRemover
from code.algorithms.minibfs import MiniBFS
from code.algorithms.minibfs_reverse import MiniBFS_reverse

# define step size for big and small loops
BIG_STEP = 10
SMALL_STEP = 6

class Hybrid():
    def __init__(self, sourcefile, size):
        self.sourcefile = sourcefile

        # set max moves according to board size
        if size == 6:
            self.max_moves = 9
        elif size == 9:
            self.max_moves = 5
        elif size == 12:
            self.max_moves = 4

        # initialize variable to remember length of moves_set
        self.moves_set_archive = []

    def run_randomise(self):
        """
        Runs randomise algorithm untill stopped with ctrl-c.
        """
        randomise = Randomise(self.sourcefile)
        moves_set = randomise.run()
        self.moves_set_archive.append(['randomise', len(moves_set)])
        return moves_set

    def run_loopremover(self, moves_set):
        """
        Runs loop remover once.
        """
        loopremover = LoopRemover(self.sourcefile, moves_set)
        moves_set = loopremover.run()
        self.moves_set_archive.append(['loopremover', len(moves_set)])
        return moves_set

    def run_minibfs(self, moves_set):
        """
        Runs mini breadth first with big step size and max moves based on board size.
        """
        global BIG_STEP
        minibfs = MiniBFS(self.sourcefile, BIG_STEP, moves_set, self.max_moves)
        moves_set = minibfs.run()
        self.moves_set_archive.append(['minibfs', len(moves_set)])
        return moves_set
    
    def run_minibfs_reverse(self, moves_set):
        """
        Runs mini breadth first reversed with small step size.
        """
        global SMALL_STEP
        minibfs = MiniBFS_reverse(self.sourcefile, SMALL_STEP, moves_set, self.max_moves)
        moves_set = minibfs.run()
        self.moves_set_archive.append(['minibfs reversed', len(moves_set)])
        return moves_set

    def run(self):
        """
        Runs hybrid algorithm with random algorithm and 3 loops of
        a forward and reversed algorithm, with loop removers in between.
        """

        # run randomise untill ctrl-c
        moves_set = self.run_randomise()
        print(f"Random: {len(moves_set)}")

        # run loopremover
        moves_set = self.run_loopremover(moves_set)
        print(f"Loopremover: {len(moves_set)}")

        for i in range(3):

            # run minibfs in steps of 10
            moves_set = self.run_minibfs(moves_set)
            print(f"Mini bfs: {len(moves_set)}")

            # run loopremover
            moves_set = self.run_loopremover(moves_set)
            print(f"Loopremover: {len(moves_set)}")

            # run minibfs reversed in steps of 6
            moves_set = self.run_minibfs_reverse(moves_set)
            print(f"Mini bfs reversed: {len(moves_set)}")

            # run loopremover
            moves_set = self.run_loopremover(moves_set)
            print(f"Loopremover: {len(moves_set)}")

        return moves_set
