from code.algorithms.bfs import BreadthFirst

class BFHybrid(BreadthFirst):
    """
    Creates Breadth First algorithm where first moves are set and goal
    is a given layout.
    """
    def __init__(self, sourcefile, goal, starting_moves):
        self.game = Game(sourcefile)
        self.archive{}
        self.goal = goal

        # run starting moves
        for choice in starting_moves:
            self.game.move(choice)
        self.game.create_layout()

        # put first possible moves in queue
        last_move = starting_moves[-1]
        self.queue = [[move] for move in self.game.find_moves(last_move)]
    
    def won_game(self):
        """
        Game is won if layout is equal to goal layout.
        """
        if self.game.board.layout.tobytes() == self.goal:
            return True
        return False