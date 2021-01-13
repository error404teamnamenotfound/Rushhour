import matplotlib.pyplot as plt
import matplotlib
#import pygame
import numpy as np

def draw_board(layout):

    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # WIDTH = 20
    # HEIGHT = 20
    # MARGIN = 5
    # pygame.init()
    # WINDOW_SIZE = [255, 255]
    # screen = pygame.display.set_mode(WINDOW_SIZE)
    # screen.fill(BLACK)

    # done = False

    # while not done:
    #     for event in pygame.event.get():  # User did something
    #         if event.type == pygame.QUIT:  # If user clicked close
    #             done = True
    #     for row in matrix:
    #         for col in row:
    #             color = WHITE
    
    # pygame.quit()

    matrix = [[ord(char) for char in row] for row in layout]

    # matplotlib.rcParams['backend'] = 'TkAgg'
    # print(matplotlib.rcParams['backend'])

    print(matrix)

    #fig = plt.figure()
    plt.matshow(matrix)
    plt.show()

    plt.savefig('test.png')
    # matrix.savefig('testt.png')