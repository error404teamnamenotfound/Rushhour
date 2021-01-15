from code.classes.game import Game
import numpy as np
import copy

class BreadthFirst():
    def __init__(self, sourcefile):
        self.game = Game(sourcefile)
        self.archive = [] # keep track of all visited nodes
        last_move = [None, 0]
        self.queue = [[move] for move in self.game.find_moves(last_move)]
        #self.queue = [[['A', -2], ['B', -2], ['C', -1], ['D', -1], ['G', -2], ['H', -1], ['F', 2], ['X', -1], ['K', -2], ['I', -3], ['L', -3], ['K', 2], ['F', -1], ['H', 3], ['X', 3]]]
        #self.queue = [[['A', -1], ['C', -1], ['G', -2], ['L', -2], ['J', -3], ['I', 2], ['H', 1], ['E', 3], ['D', -1], ['H', -1], ['I', -3], ['H', 1], ['E', -2], ['J', 3], ['E', 2], ['L', 2], ['X', 3]]] # all the valid moves of one layer
    
    def get_moves_set(self):
        """
        Returns first item in queue.
        """
        return self.queue.pop(0)

    def try_moves(self):
        """
        Moves cars according to set of moves and creates new layout.
        """
        pass

    def add_to_queue(self, moves_set):
        """
        Finds new moves and adds to queue.
        """

        # find new possible moves
        new_moves = self.game.find_moves(copy.deepcopy(moves_set[-1]))

        # add new moves series to queue
        for new_move in new_moves:
            self.queue.append(moves_set + [new_move])

    def run(self):

        while True:
        #for i in range(20):

            if len(self.queue) % 1000 == 0:
                print(len(self.queue[0]))

            # get first move from queue
            moves_set = self.get_moves_set()

            #print(moves_set)

            # try moves
            for choice in moves_set:
                #print(choice)
                self.game.move(choice)

            # create new layout
            self.game.board.create_layout()
            #self.game.board.draw_board()
            
            # check for win
            if self.game.win():
                
                print("we won")
                self.game.board.draw_board()

                # return winning set of moves
                return moves_set

            # continue if layout is not in archive
            if not any(np.array_equal(self.game.board.layout, old) for old in self.archive):

                # save layout in archive
                self.archive.append(self.game.board.layout)

                # add new moves sets to queue
                self.add_to_queue(moves_set)
            
            # first go back to original layout
            #print(moves_set)
            moves_set.reverse()
            #print(moves_set)
            for choice in moves_set:
                #print(f"go back {choice[0], -choice[1]}")
                self.game.move([choice[0], -choice[1]])
            



# def breadth_first_search(self, graph, root): 
# # keep track of explored nodes
#     explored = []
#     # keep track of all the paths to be checked
#     queue = [[start]]
 
#     # return path if start is goal
#     if start == goal:
#         return "That was easy! Start = goal"
 
#     # keeps looping until all possible paths have been checked
#     while queue:
#         # pop the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         node = path[-1]
#         if node not in explored:
#             neighbours = graph[node]
#             # go through all neighbour nodes, construct a new path and
#             # push it into the queue
#             for neighbour in neighbours:
#                 new_path = list(path)
#                 new_path.append(neighbour)
#                 queue.append(new_path)
#                 # return path if neighbour is goal
#                 if neighbour == goal:
#                     return new_path
 
#             # mark node as explored
#             explored.append(node)
 
#     # in case there's no path between the 2 nodes
#     return "So sorry, but a connecting path doesn't exist :("
 
# bfs_shortest_path(graph, 'G', 'D')  # returns ['G', 'C', 'A', 'B', 'D']


# if __name__ == '__main__':
#     graph = possible moves
#     breadth_first_search(graph, 0)AE,-1