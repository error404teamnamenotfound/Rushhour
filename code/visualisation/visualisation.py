import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib
from code.classes.game import Game

def visualize(sourcefile, outputfile):

    # initialize figure and images list
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

    # create first layout
    game.board.create_layout()

    # change matrix to numbers
    matrix = np.array([[ord(letter) - 64 for letter in row] for row in game.board.layout])
    indices = np.where(matrix == 31)
    matrix[indices] = 0

    # create first image
    im = plt.imshow(matrix, animated=True, cmap ='terrain_r')
    ims.append([im])

    # move and add new images per layout
    for move in moves_set:
        game.move(move)
        game.board.create_layout()
        matrix = np.array([[ord(letter) - 64 for letter in row] for row in game.board.layout])
        indices = np.where(matrix == 31)
        matrix[indices] = 0
        im = plt.imshow(matrix, animated=True, cmap='terrain_r')
        ims.append([im])

    # create animation
    ani = animation.ArtistAnimation(fig, ims, interval=400, blit=True, repeat_delay=10000)
    ani.save(f'{outputfile}.gif')