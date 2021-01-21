import csv
from code.classes.game import Game
from code.algorithms.bfs import BreadthFirst

# MAX = 10
class retroactivity():
    def __init__(self, outputfile):
        self.move_set = {}
        with open(outputfile) as move_set:
            csv_reader = csv.reader(move_set)
            next()
            for i, row in csv_reader:
                self.move_set[i] = row


    def run(self):
        # global MAX
        # count = 0
        # while True:
        # move_set = 
        # move_set = list(self.move_set)[MAX:]
        # for move in move_set:
            # self.move(move)
        # 
        # create layout
        # layout = self.board.layout
        # bfs = BreathFirst(Sourcefile??(layout??))
        # move_set = bfs.run
        # check for win??

        # if move_set < MAX:
            # best_moves.append(move_set)

        # win = layout

        # return reverse(best_moves)
        pass


    def win(self):
        pass


