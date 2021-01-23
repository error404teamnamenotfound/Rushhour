import csv
from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid

MAX = 7
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

            # try:
            #     if final_moves_set[-1] == new_moves_set:
            #         final_moves_set.pop()
            # except IndexError:
            #     pass

            # check if goal was reached or full game was won
            won = bfs.won_game()
            print(f"won: {won}")

            # if new moves set is shorter, run bfs from there
            if len(new_moves_set) < MAX:
                self.moves_set = self.moves_set + new_moves_set

            # if full game was won, new moves set is your final set
            elif won == 1:
                final_moves_set = new_moves_set

            # if goal was not reached in less steps, run bfs from MAX steps less again
            else:
                final_moves_set = new_moves_set + final_moves_set
            
            # # append or insert moves based on won
            # won = bfs.won_game()
            # if won == 1:
            #     final_moves_set = new_moves_set
            # else:
            #     final_moves_set = new_moves_set + final_moves_set

        return final_moves_set



