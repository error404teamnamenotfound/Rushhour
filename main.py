import csv, sys

from code.algorithms.bfs import BreadthFirst
from code.algorithms.randomise import Randomise
from code.algorithms.minibfs import MiniBFS
from code.algorithms.hybrid import Hybrid

from code.visualisation.visualisation import Visualize


if __name__ == '__main__':

    # initialize MAX for randomise
    MAX = 0
    
    # correct input
    if len(sys.argv) < 3:
        print("command: python main.py breadthfirst 6x6_1")
        sys.exit(1)

    # get algorithm and bord
    algorithm_choice = sys.argv[1]
    board_choice = sys.argv[2]
    
    # MAX for randomise
    if len(sys.argv) == 4:
        MAX = sys.argv[3]

    # different possible algorithms
    algorithms = {
    "randomise" : Randomise,
    "breadthfirst" : BreadthFirst,
    "hybrid" : Hybrid
    }

    # run algorithm
    if algorithm_choice == 'breadthfirst':
        moves_set = algorithms[algorithm_choice](f'data/Rushhour{board_choice}.csv').run()
    
    else:
        if not MAX:
            MAX = 1000

        moves_set = algorithms[algorithm_choice](f'data/Rushhour{board_choice}.csv', MAX).run()

    # write moves set to outputfile
    with open(f'output/{board_choice}/output{board_choice}_{algorithm_choice}_{len(moves_set)}.csv', 'w', newline='') as outputfile:
        fieldnames = ['car', 'move']
        writer = csv.writer(outputfile)
        writer.writerow(fieldnames)
        writer.writerows(moves_set)

    # visualize output
    Visualize(f'data/Rushhour{board_choice}.csv', f'output/{board_choice}/output{board_choice}_{algorithm_choice}_{len(moves_set)}.csv').run()
