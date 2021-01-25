# Rush Hour

Rush Hour is a sliding puzzle in which the aim is to get the red car to the exit. In a field of x high and x wide, several cars (two units) and trucks (three units) block the exit, preventing the red car from reaching that exit. The vehicles cannot change their direction from vertical to horizontal and vice versa. The difficulty of the game is determined by the fact that there is not one straight line to the end goal. For instance, sometimes the red has to move backwards to clear a path for a later state.

## To get started

### Requirements

This code is written in python 3.8. To run this code successfully some required packages are necessary. These are easy to install with the following code:

`pip install -r requirements.txt`

### Usage

To run an breadthfirst search use:
`python3 main.py {algorithm choice} {board choice}`

If you want to run Randomise or Hybrid, you can add a MAX for the number of moves a random can do:
`python3 main.py {algorithm choice} {board choice} {MAX: 1000}`
    
    If MAX if not given the MAX will be pre-set to 1000

### Structure

- /code/ : includes all the code

    - /code/algorithms/ : methods to solve the game

    - /code/classes/ : classes to create a game

- /data/ : data documents to create a board and the beginning position of the cars

- /design/ : design document with classes

- /output/ : csv files with moves set and a matplotlib visualisation per board

### Output

This is an example of the visualisation output of board 6x6_1 with the Breadth First Search algorithm. It illustrates the shortest solution to win the game.

![alt text](https://github.com/error404teamnamenotfound/Rushhour/blob/main/output/output6x6_1_breadthfirst.csv.gif)

### Authors

- Stef Grijpma
- Mylène van der Maas
- Melody Kaagman
