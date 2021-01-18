import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib
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
    #matrix = np.array([[row - 64] for row in game.board.layout])
    matrix = np.array([[ord(letter) - 64 for letter in row] for row in game.board.layout])
    indices = np.where(matrix == 31)
    matrix[indices] = red

    indices = np.where(matrix == 24)
    matrix[indices] = 19
    # matrix = [[ord(letter) for letter in row] for row in game.board.layout]
    
    # print(matrix)

    # matrix = [[[255] for letter in row if letter == 88] for row in game.board.layout]

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         if matrix[i][j] == 88:
    #             print('X')
    #             matrix[i][j] = 13
            
    # print(matrix)

    # masked_array = np.ma.masked_where(matrix == 88, matrix)
    # cmap = matplotlib.cm.hot

    # cmap.set_bad(color='red', alpha = None)

    im = plt.imshow(matrix, animated=True, cmap ='Reds')
    ims.append([im])

    # move and add new layout to ims
    for move in moves_set:
        game.move(move)
        game.board.create_layout()
        #matrix = [[letter - 64 for letter in row] for row in game.board.layout]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
                
        #         if matrix[i][j] == 88:
        #             print('X')
        #             matrix[i][j] = 13
        #         else: 
        #             matrix[i][j] -= 64
        matrix = np.array([[ord(letter) - 64 for letter in row] for row in game.board.layout])
        indices = np.where(matrix == 31)
        matrix[indices] = 0

        indices = np.where(matrix == 24)
        matrix[indices] = 19
        # masked_array = np.ma.masked_where(matrix == 88, matrix)
        # cmap = matplotlib.cm.hot

        # cmap.set_bad(color='red', alpha=None)
        print(matrix)
        im = plt.imshow(matrix, animated=True, cmap='Reds')
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=900, blit=True, repeat_delay=10000)
    ani.save(f'{outputfile}.gif')