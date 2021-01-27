# Algorithms

## Randomise
- chooses a random valid move untill the game is won
- repeats algorithm untill stopped with `ctrl + C`
- with branch and bound: next run will not exceed length of smallest moves set found so far
- if no MAX moves is given, the MAX is set on 1000
    - we found that every board can be solved quite quickly in less than 1000 moves and moves sets of more than 1000 moves are useless for our other algorithms
    - because of the branch and bound, it might take some time untill a moves set (smaller than MAX) is found. 

## Breadth Firt Search
- goes through every layer of the decision three
- stops when the game is won

## Hybrid
- a combination algorithm of randomise, a loopremover and small breadth firsts

#### loopremover
- removes all steps between double layouts

#### minibfs
- goes forward through a moves set in steps of 10 and uses breadth first to try to find a smaller path of moves
    - 10 steps forward were chosen to quickly go through the full moves set (big steps) to remove the biggest nonsense moves and reach a win earlier (trial and error showed that the first time of running a mini bfs forward with big steps, the final board was reached in an average of 30 steps less than the original moves set).
    - because the state space of 9x9 and 12x12 boards is too big to reach in reasonable time, the max_moves are set to relatively 5 and 4 (found to be reasonable by trial and error). This max_moves hold that the breadth first has to search untill layer {max_moves} in the decision tree.

#### minibfs_reversed
- goes backwards through a moves set in small steps of 6 and uses breadth first to try and find a smaller path of moves
    - backwards so that the algorithm is focussing on trying to reach the final layout
    - steps of 6 to get smaller nonsense moves out
    - same max_moves as minibfs

#### bfs_hybrid
- breadth first with extra win statements
    - the normal breadth first algorithm only stops if the game was won, but the bfs hybrid also stops if a given goal layout was reached
    - this algorithm accepts a list of starting moves and searches from there to the goal layout


