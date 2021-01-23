import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib import cm
import numpy as np
import matplotlib
from code.classes.game import Game

class Visualize:
    
    def __init__(self, sourcefile, outputfile):
        # initialize figure and images list
        self.fig = plt.figure()
        self.ims = []
        self.outputfile = outputfile

        # read outputfile
        with open(outputfile, "r") as reader:
            datafile = csv.reader(reader)
            next(datafile)
            self.moves_set = []
            for row in datafile:
                self.moves_set.append([row[0], int(row[1])])

        # create new game
        self.game = Game(sourcefile)

        # create first layout
        self.game.board.create_layout()

        # create color map
        possible_colors = ["darkorange", "darkgreen", "gold","navy", "indigo", "steelblue"]
        colors = ["white", "red"]
        for i in range(len(self.game.board.cars) - 1):
            colors.append(possible_colors[i % len(possible_colors)])
        cmap = ListedColormap(colors)

        # change matrix to numbers
        matrix = np.array([[ord(letter) - 63 for letter in row] for row in self.game.board.layout])
        indices = np.where(matrix == 32)
        xx = np.where(matrix == 25)
        matrix[indices] = 0
        matrix[xx] = 1

        # create first image
        plt.xticks([])
        plt.yticks([])
        im = plt.imshow(matrix, animated=True, cmap=cmap)
        self.ims.append([im])

        # move and add new images per layout
        for move in self.moves_set:
            self.game.move(move)
            self.game.board.create_layout()
            matrix = np.array([[ord(letter) - 63 for letter in row] for row in self.game.board.layout])
            indices = np.where(matrix == 32)
            matrix[indices] = 0
            xx = np.where(matrix == 25)
            matrix[xx] = 1
            im = plt.imshow(matrix, animated=True, cmap=cmap)
            self.ims.append([im])

        # create animation
        ani = animation.ArtistAnimation(self.fig, self.ims, interval=400, blit=True, repeat_delay=10000)
        ani.save(f'{self.outputfile}.gif')