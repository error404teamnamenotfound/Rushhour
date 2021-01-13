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

    def __str__(self):
        return f"Car {self.name} on ({self.row},{self.col})"

    
    # def move(self, direction):
    #     """
    #     Moves car horizontally or vertically.
    #     """
    #     if self.orientation == 'H':
    #         self.col += direction
    #     elif self.orientation == 'V':
    #         self.row += direction