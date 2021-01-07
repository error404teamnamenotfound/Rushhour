import csv
import numpy as np
import re
from code.classes.car import Car

class Board():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)

        # get board size from filename
        result = re.search('Rushhour(.*)x', source_file)
        self.size = int(result.group(1))

        self.layout = self.create_layout()


    def load_cars(self, source_file):

        cars_list = []

        with open(source_file, "r") as reader:
            datafile = csv.reader(reader)

            # go over rows in datafile
            next(datafile)
            for row in datafile:
                car = Car(row[0], row[1], row[2], row[3], row[4])
                cars_list.append(car)

        return cars_list

    def create_layout(self):
        self.layout = np.chararray((self.size, self.size), unicode=True)
        self.layout[:] = '_'

        for car in self.cars:
            if car.orientation == "H":
                for i in range(car.length):
                    self.layout[car.row][car.col + i] = car.name
            elif car.orientation == "V":
                for i in range(car.length):
                    self.layout[car.row + i][car.col] = car.name
            
        return self.layout

    def draw_board(self):
        for row in self.layout:
            for block in row:
                # if block == 0:
                #     print("_ ", end="")
                # else:
                print(f"{block} ", end="")
            print("")