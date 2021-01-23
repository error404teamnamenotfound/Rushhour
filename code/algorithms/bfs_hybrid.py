from code.algorithms.bfs import BreadthFirst

from code.classes.game import Game

class BFHybrid(BreadthFirst):
    """
    Creates Breadth First algorithm where first moves are set and goal
    is a given layout.
    """
    def __init__(self, sourcefile, goal, starting_moves):
        self.game = Game(sourcefile)
        self.archive = {}
        self.goal = goal

        # run starting moves
        for choice in starting_moves:
            self.game.move(choice)
        self.game.board.create_layout()
        self.game.board.draw_board()

        # put first possible moves in queue
        if starting_moves:
            last_move = starting_moves[-1]
        else:
            last_move = [None, 0]
        self.queue = [[move] for move in self.game.find_moves(last_move)]

        # if no moves possible find moves without last move
        if not self.queue:
            last_move = [None, 0]
            self.queue = [[move] for move in self.game.find_moves(last_move)]
    
    def won_game(self):
        """
        Game is won if layout is equal to goal layout.
        """
        if self.game.win():
            return 1
        elif self.game.board.layout.tobytes() == self.goal:
            return 2
        return False