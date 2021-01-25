# Algorithms

## Randomise
- chooses a random valid move untill the game is won
- works with branch and bound: saves lowest moves set
- to stop this algorithm press `ctrl + C`

## Breadth Firt Search
- goes through every layer of the decision three
- stops when the game is won

## Hybrid algorithm 
- a combination algorithm with multiple algorithms 

### Parameters

#### minibfs
- looks if 10 steps can be cut to 5
    - "Ten steps are chosen for a shorter runtime on 9x9_5, 9x9_6 and 12x12_7. This because the possibilities on these bords are exponentiely growing and the cars have a lot more options than on the 6x6 bords."

#### minibfs_reversed
- looks if 6 steps can be cut to 5
    - "the reversed begins at the end layout and works backwords. To make sure the same move_set is not being used two times another stepsize at least 3 away is chosen. "

#### loopremover
- removes all steps between dubble layouts

#### bfshybrid
- Has a extra goal
    - "The normal bsf only stops if the end layout is reached, but the hybrid also stops if the end layout is reached withhout this being the finish."


