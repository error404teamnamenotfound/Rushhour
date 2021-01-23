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
        
        final_moves_set = []
        while self.moves_set:
            
            # get final layout
            for choice in self.moves_set:
                self.game.move(choice) 
            self.game.board.create_layout()
            layout = self.game.board.layout.tobytes()
            print("layout created")
            
            # run breadthfirst from starting moves to final layout
            if len(self.moves_set) >= MAX:
                print(len(self.moves_set))
                del self.moves_set[-MAX:]
                print(f"moves:{len(self.moves_set)}")
                # self.moves_set = self.moves_set[len(self.moves_set)-MAX:]
            else:
                self.moves_set.clear()
                
            bfs = BFHybrid(self.sourcefile, layout, self.moves_set)
            new_moves_set = bfs.run()

            try:
                if final_moves_set[len(final_moves_set)-1] == new_moves_set:
                    final_moves_set.pop()
            except IndexError:
                pass
            
            # append or insert moves based on won
            won = bfs.won_game()
            final_moves_set = new_moves_set + final_moves_set

        return final_moves_set



