import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib import cm
import numpy as np
import matplotlib
from code.classes.game import Game

ASCII = 63
VALUE__ = 32
VALUE_X = 25

class Visualize:
    
    def __init__(self, sourcefile, outputfile):

        # initialize variables
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

        # removes axes in images
        plt.xticks([])
        plt.yticks([])

        # create color map
        self.colormap()


    def colormap(self):
        """ 
        Makes the color map based on number of cars in game. 
        """

        # colors for vehicles
        possible_colors = ["darkorange", "darkgreen", "gold","navy", "indigo", "steelblue"]

        # colors for blank spaces and target car
        colors = ["white", "red"]

        # look for the highest ascii value from the cars
        last_car = max([ord(car.name[-1]) - ASCII for car in list(self.game.board.cars.values())[:-1]])

        # add color to colormap for all the cars
        for i in range(last_car - 1):
            colors.append(possible_colors[i % len(possible_colors)])
        self.cmap = ListedColormap(colors)

    def matrix_to_numbers(self):
        """
        Changes the layout to a matrix of ascii numbers to match the colormap.
        """

        # loop over layout to change to numbers
        matrix = np.array([[ord(letter) - ASCII for letter in row] for row in self.game.board.layout])
        indices = np.where(matrix == VALUE__)
        xx = np.where(matrix == VALUE_X)
        matrix[indices] = 0
        matrix[xx] = 1

        return matrix

    def create_image(self, matrix):
        """
        Creates images of matrices in matplotlib.
        """
     
        im = plt.imshow(matrix, animated=True, cmap=self.cmap)
        self.ims.append([im])

    def run(self):
        """ 
        Runs algorithm to create a gif of a Rush Hour game. 
        """

        # create first layout
        matrix = self.matrix_to_numbers()
        self.create_image(matrix)

        # create image per move in game
        for move in self.moves_set:
            self.game.move(move)
            self.game.board.create_layout()
            matrix = self.matrix_to_numbers()
            self.create_image(matrix)

        # create animation and add it to outputmap
        ani = animation.ArtistAnimation(self.fig, self.ims, interval=400, blit=True, repeat_delay=10000)
        ani.save(f'{self.outputfile}.gif')