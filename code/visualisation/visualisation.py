import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from code.classes.game import Game

def visualize(sourcefile, outputfile):
    fig = plt.figure()
    ims = []

    # read outputfile
    with open(outputfile, "r") as reader:
        datafile = csv.reader(reader)
        next(datafile)
        moves_set = []
        for row in datafile:
            moves_set.append([row[0], int(row[1])])

    # create new game
    game = Game(sourcefile)

    # add first board to ims
    game.board.create_layout()
    matrix = [[ord(letter) for letter in row] for row in game.board.layout]
    im = plt.imshow(matrix, animated=True)
    ims.append([im])

    # move and add new layout to ims
    for move in moves_set:
        game.move(move)
        game.board.create_layout()
        matrix = [[ord(letter) for letter in row] for row in game.board.layout]
        im = plt.imshow(matrix, animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True, repeat_delay=10000)
    ani.save(f'{outputfile}.gif')