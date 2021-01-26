from code.classes.game import Game
from code.algorithms.randomise import Randomise


class LoopRemover():
    """
    Algorithm that takes a moves set, finds which layouts are visited
    twice and removes all moves in between those layouts.
    """
    def __init__(self, sourcefile, moves_set):
        self.sourcefile = sourcefile
        self.moves_set = moves_set

    def find_double_layouts(self):
        """
        Creates all layouts for a moves set and finds duplicates.
        """

        # create a new game, dict for layouts and key pairs list
        game = Game(self.sourcefile)
        layout_dict = {}
        key_pairs = []
        
        # save layout per move
        for i in range(len(self.moves_set)):
            game.move(self.moves_set[i])
            game.board.create_layout()
            layout = game.board.layout

            # if layout is already in dict, save keys as key pair
            for key in layout_dict:
                if layout.tobytes() == layout_dict[key].tobytes():
                    key_pairs.append([key, i])

            layout_dict[i] = layout
        
        return key_pairs

    def run(self):
        """
        Runs loopremover algorithm.
        """
        while self.moves_set:

            key_pairs = self.find_double_layouts()

            # stop if there are no double layouts left
            if not key_pairs:
                break
            
            # sort key pairs on length of move set (largest loop first)
            key_pairs_sort = sorted(key_pairs, key=lambda key_pairs:key_pairs[1]-key_pairs[0], reverse=True)
            
            # delete moves of largest layout loop
            del self.moves_set[(key_pairs_sort[0][0] + 1): key_pairs_sort[0][1] + 1]
            
        return self.moves_set

        

        