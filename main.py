import csv
import sys 

from code.algorithms.bfs import BreadthFirst
from code.algorithms.randomise import Randomise
from code.algorithms.hybrid import Hybrid

from code.visualisation.visualisation import visualize


if __name__ == '__main__':

    # find algorithm and board input
    try:
        algorithm_choice = sys.argv[1]
        board_choice = sys.argv[2]
    except: 
        algorithm_choice = "breadthfirst"
        board_choice = '6x6_1'
    
    # different possible algorithms
    algorithms = {
    "randomise" : Randomise,
    "breadthfirst" : BreadthFirst,
    "hybrid": Hybrid
    }
    
    # run algorithm
    moves_set = algorithms[algorithm_choice](f'data/Rushhour{board_choice}.csv').run()
    
    # write moves set to outputfile
    with open(f'output/output{board_choice}_{algorithm_choice}_{len(moves_set)}.csv', 'w', newline='') as outputfile:
        fieldnames = ['car', 'move']
        writer = csv.writer(outputfile)
        writer.writerow(fieldnames)
        writer.writerows(moves_set)
    
    # # print output
    # print(moves_set)
    
    # # visualize output
    # visualize(f'data/Rushhour{board_choice}.csv', f'output/output{board_choice}_{algorithm_choice}.csv')
