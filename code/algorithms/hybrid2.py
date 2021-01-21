import csv
from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid

MAX = 10
class Hybrid2():
    def __init__(self, sourcefile, outputfile):

        self.game = Game(sourcefile)
        self.sourcefile = sourcefile

        # get moves set
        with open(outputfile, "r") as reader:
            datafile = csv.reader(reader)
            next(datafile)
            self.moves_set = []
            for row in datafile:
                self.moves_set.append([row[0], int(row[1])])

        print("loaded")

    def run(self):
        global MAX
        #starting_moves = self.moves_set

        while self.moves_set:
            
            # get final layout
            for move in self.moves_set:
                self.game.move(move) 
            self.game.board.create_layout()

            print("layout created")
            
            # run breadthfirst from starting moves to final layout
            self.moves_set = self.moves_set[:-MAX]
            layout = self.game.board.layout.tobytes()
            bfs = BFHybrid(self.sourcefile, layout, self.moves_set)
            new_moves_set = bfs.run()

            # append or insert moves based on won
            won = bfs.won_game()
            if won == 1:
                final_moves_set = [self.moves_set + new_moves_set]
            elif won == 2:
                final_moves_set.insert(0, new_moves_set)

            if len(new_moves_set) < MAX:
                # TODO
                self.moves_set = self.moves_set + new_moves_set

            print(new_moves_set)

        return final_moves_set



