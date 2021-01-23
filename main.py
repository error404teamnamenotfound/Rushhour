import csv
import sys 

from code.algorithms.bfs import BreadthFirst
from code.algorithms.randomise import Randomise
from code.algorithms.hybrid import Hybrid
from code.algorithms.hybrid2 import Hybrid2

from code.visualisation.visualisation import Visualize


if __name__ == '__main__':

    # hybrid2 = Hybrid2(f'data/Rushhour9x9_6.csv', f'output/output_6_85.csv')
    # moves_set = hybrid2.run()
    # print(moves_set)
    # print(len(moves_set))

    # find algorithm and board input
    # try:
    #     algorithm_choice = sys.argv[1]
    #     board_choice = sys.argv[2]
    # except: 
    #     algorithm_choice = "breadthfirst"
    #     board_choice = '6x6_1'
    
    # # different possible algorithms
    # algorithms = {
    # "randomise" : Randomise,
    # "breadthfirst" : BreadthFirst,
    # "hybrid": Hybrid
    # }
    
    # # run algorithm
    # moves_set = algorithms[algorithm_choice](f'data/Rushhour{board_choice}.csv').run()
    
    # write moves set to outputfile
    # with open(f'output/output{board_choice}_{algorithm_choice}_{len(moves_set)}.csv', 'w', newline='') as outputfile:
    #     fieldnames = ['car', 'move']
    #     writer = csv.writer(outputfile)
    #     writer.writerow(fieldnames)
    #     writer.writerows(moves_set)
    
    # # # print output
    # # print(moves_set)
    
    # # # visualize output
    # Visualize(f'data/Rushhour{board_choice}.csv', f'output/output{board_choice}_{algorithm_choice}.csv')

    Visualize(f'data/Rushhour9x9_4.csv', f'output/output9x9_4_randomise.csv')

