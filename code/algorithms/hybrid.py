import csv
from code.classes.game import Game

class Hybrid():
    def __init__(self, sourcefile, outputfile):

        #self.game = Game(sourcefile)
        #self.moves_dict = {}

        self.sourcefile = sourcefile
        self.outputfile = outputfile

        # read outputfile
        with open(outputfile, "r") as reader:
            datafile = csv.reader(reader)
            next(datafile)
            self.moves_set = []
            for row in datafile:
                self.moves_set.append([row[0], int(row[1])])

    def run(self):

        while True:
        #for i in range(2):

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
                        #print(self.moves_dict[key])
                        #print(layout)
                    #key = self.moves_dict[layout]
                    #key_pairs.append([self.moves_dict[layout], i]

                self.moves_dict[i] = layout

            if not key_pairs:
                break
            
            key_pairs_sort = sorted(key_pairs, key=lambda key_pairs:key_pairs[1]-key_pairs[0], reverse=True)
            #print(key_pairs_sort)
            
            #print(len(self.moves_set))
            del self.moves_set[(key_pairs_sort[0][0] + 1): key_pairs_sort[0][1] + 1]
            #print(len(self.moves_set))
            #self.moves_set = self.moves_set[:key_pairs_sort[1], key_pairs_sort[0]:]

            #print(len(key_pairs_sort))

        #print(len(self.moves_set))
        #print(self.moves_set)
        return self.moves_set

        

        