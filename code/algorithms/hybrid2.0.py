import csv
from code.classes.game import Game
from code.algorithms.bfs import BreadthFirst

MAX = 10
class Retroactivity():
    def __init__(self, sourcefile, outputfile):
        self.move_set = {}
        with open(outputfile) as move_set:
            csv_reader = csv.reader(move_set)
            next()
            for i, row in csv_reader:
                self.move_set[i] = row
        self.sourcefile = sourcefile


    def run(self):
        global MAX
        # while True:
        # move_set = 
        # stappen uitvoeren
        for move in self.move_set:
            self.game.move(move) 
        # create layout
        move_set = list(self.move_set)[MAX:]
        # layout = self.board.layout
        # bfs = BreathFirst(self.sourcefile, layout, move_set)
        # move_set = bfs.run
        # check for win??

        # if move_set < MAX:
            # best_moves.append(move_set)

        # win = layout

        # return reverse(best_moves)
        pass


    def win(self):
        pass


