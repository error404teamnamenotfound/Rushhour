import csv
import sys 

from code.algorithms.bfs import BreadthFirst
from code.algorithms.randomise import Randomise
#from code.algorithms.hybrid import Hybrid
from code.algorithms.minibfs import MiniBFS
from code.algorithms.hybrid3 import Hybrid3

from code.visualisation.visualisation import Visualize


if __name__ == '__main__':

    hybrid3 = Hybrid3('data/Rushhour12x12_7.csv')
    moves_set = hybrid3.run()
    print(f"moves_set; {moves_set}")
    print(f"len moves_set; {len(moves_set)}")

    # minibfs = MiniBFS(f'data/Rushhour6x6_1.csv', 10, f'output/output_1_54.csv')
    # moves_set = minibfs.run()
    # print(f"moves_set; {moves_set}")
    # print(f"len moves_set; {len(moves_set)}")

    # hybrid = Hybrid(f'data/Rushhour9x9_5.csv', f'output/output9x9_5_hybrid2_184.csv')
    # moves_set = hybrid.run()
    # print(f"moves_set; {moves_set}")
    # print(f"len moves_set; {len(moves_set)}")

    # # find algorithm and board input
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

    
    # # write moves set to outputfile
    # with open(f'output/output{board_choice}_{algorithm_choice}_{len(moves_set)}.csv', 'w', newline='') as outputfile:
    #     fieldnames = ['car', 'move']
    #     writer = csv.writer(outputfile)
    #     writer.writerow(fieldnames)
    #     writer.writerows(moves_set)

    with open(f'output/output12x12_7_hybrid3_{len(moves_set)}.csv', 'w', newline='') as outputfile:
        fieldnames = ['car', 'move']
        writer = csv.writer(outputfile)
        writer.writerow(fieldnames)
        writer.writerows(moves_set)
    
    # # # print output
    # # print(moves_set)
    
    # # # visualize output
    # Visualize(f'data/Rushhour{board_choice}.csv', f'output/output{board_choice}_{algorithm_choice}.csv')

    Visualize(f'data/Rushhour12x12_7.csv', f'output/output12x12_7_hybrid3_{len(moves_set)}.csv')

