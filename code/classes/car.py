class Car():
    """
    Creates Car object.
    """
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = int(col) - 1
        self.row = int(row) - 1
        self.length = int(length)

