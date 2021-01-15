from code.classes.game import Game
import numpy as np
import copy

class BreadthFirst():
    def __init__(self, sourcefile):
        self.game = Game(sourcefile)
        self.archive = [] # keep track of all visited nodes
        last_move = [None, 0]
        self.queue = [[move] for move in self.game.find_moves(last_move)] # all the valid moves of one layer
        print(self.queue)
    
    def run(self):

        # keeps looping until all possible moves have been checked
        while self.queue:

            # print(len(self.queue[-1]))

            # get first move from queue
            moves_set = self.queue.pop(0)

            # try moves
            for choice in moves_set:
                self.game.move(choice)

            # create new layout
            self.game.board.create_layout()

            # check for win
            if self.game.win():
                
                print("we won")
                self.game.board.draw_board()

                # return winning set of moves
                return moves_set
            
            # print(np.array(self.game.board.layout))
            # print(np.array(self.archive))
            # # continue if layout not in archive
            # if np.array(self.game.board.layout) not in np.array(self.archive):

                
            # save layout in archive
            self.archive.append(self.game.board.layout)

            # find new possible moves
            new_moves = self.game.find_moves(copy.deepcopy(moves_set[-1]))

            # add new moves series to queue
            for new_move in new_moves:
                self.queue.append(moves_set + [new_move])
            
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