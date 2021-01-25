import csv
from code.classes.game import Game
from code.algorithms.randomise import Randomise

class Hybrid():
    def __init__(self, sourcefile, moves_set):
        self.sourcefile = sourcefile
        # print('Randomise:')
        # Random = Randomise(sourcefile)
        # self.moves_set = Random.run()

        # get moves set
        # with open(outputfile, "r") as reader:
        #     datafile = csv.reader(reader)
        #     next(datafile)
        #     self.moves_set = []
        #     for row in datafile:
        #         self.moves_set.append([row[0], int(row[1])])

        self.moves_set = moves_set

    def run(self):
        print('hybrid:')

        while True:

            key_pairs = []

            game = Game(self.sourcefile)
            self.moves_dict = {}
            
            # save layout per move
            for i in range(len(self.moves_set)):
                game.move(self.moves_set[i])
                game.board.create_layout()
                layout = game.board.layout

                for key in self.moves_dict:
                    if layout.tobytes() == self.moves_dict[key].tobytes():
                        key_pairs.append([key, i])

                self.moves_dict[i] = layout

            if not key_pairs:
                break
            
            # decending list of all double layouts
            key_pairs_sort = sorted(key_pairs, key=lambda key_pairs:key_pairs[1]-key_pairs[0], reverse=True)
            
            # delete all steps between same layouts
            del self.moves_set[(key_pairs_sort[0][0] + 1): key_pairs_sort[0][1] + 1]
            

        return self.moves_set

        

        