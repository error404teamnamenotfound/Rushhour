import csv
from code.classes.game import Game
from code.algorithms.bfs_hybrid import BFHybrid

class MiniBFS():
    def __init__(self, sourcefile, step_size, moves_set):

        #self.game = Game(sourcefile)
        self.game = Game(sourcefile)
        self.sourcefile = sourcefile

        #get moves set
        # with open(outputfile, "r") as reader:
        #     datafile = csv.reader(reader)
        #     next(datafile)
        #     self.moves_set = []
        #     for row in datafile:
        #         self.moves_set.append([row[0], int(row[1])])

        # get step size and moves set
        self.step_size = step_size
        self.moves_set = moves_set

        

        print("loaded")

    def run(self):

        final_moves_set = []
        goal_moves = []

        while self.moves_set:
            
            
            if len(self.moves_set) >= self.step_size:
                print(len(self.moves_set))
                goal_moves = self.moves_set[:self.step_size]
                print(len(goal_moves))
                #old_set = self.moves_set[:self.step_size]
                del self.moves_set[:self.step_size]
                print(f"moves:{len(self.moves_set)}")
                # self.moves_set = self.moves_set[len(self.moves_set)-MAX:]
            else:
                self.step_size = len(self.moves_set)
                goal_moves = self.moves_set[:]
                self.moves_set.clear()

            # get goal layout
            #game = Game(self.sourcefile)
            for choice in goal_moves:
                self.game.move(choice)
            self.game.board.create_layout()
            layout = self.game.board.layout
            print("layout created")
            
            # run breadth first hybrid version
            bfs = BFHybrid(self.sourcefile, layout, final_moves_set, self.step_size)
            new_moves_set = bfs.run()

            # check if goal was reached or full game was won
            won = bfs.won_game()
            print(f"won: {won}")

            # if full game was won, add to final moves set and stop
            if won == 1:
                final_moves_set = final_moves_set + new_moves_set
                return final_moves_set

            # if shorter moves set found, add to self.moves_set and start over
            elif won == 2:
                final_moves_set = final_moves_set + new_moves_set

            # if max steps was reached, keep old set of moves
            elif won == 3:
                final_moves_set = final_moves_set + goal_moves

        return final_moves_set
        
        # final_moves_set = []
        # while self.moves_set:
            
        #     # get goal layout
        #     game = Game(self.sourcefile)
        #     for choice in self.moves_set:
        #         game.move(choice) 
        #     game.board.create_layout()
        #     layout = game.board.layout
        #     print("layout created")
            
        #     # run breadthfirst from starting moves to final layout
        #     if len(self.moves_set) >= MAX:
        #         print(len(self.moves_set))
        #         old_set = self.moves_set[-MAX:]
        #         del self.moves_set[-MAX:]
        #         print(f"moves:{len(self.moves_set)}")
        #         # self.moves_set = self.moves_set[len(self.moves_set)-MAX:]
        #     else:
        #         MAX = len(self.moves_set)
        #         old_set = self.moves_set[:]
        #         self.moves_set.clear()

                
        #     bfs = BFHybrid(self.sourcefile, layout, self.moves_set, MAX)
        #     new_moves_set = bfs.run()

        #     # check if goal was reached or full game was won
        #     won = bfs.won_game()
        #     print(f"won: {won}")

        #     # if new moves set is shorter, run bfs from there
        #     if len(new_moves_set) < MAX and won != 3:
        #         self.moves_set = self.moves_set + new_moves_set

        #     # if full game was won, new moves set is your final set
        #     elif won == 1:
        #         final_moves_set = new_moves_set

        #     # if MAX steps was reached, keep old set of moves
        #     elif won == 3:
        #         final_moves_set = old_set + final_moves_set

        #     # if goal was not reached in less steps, run bfs from MAX steps less again
        #     else:
        #         final_moves_set = new_moves_set + final_moves_set

        #return final_moves_set



