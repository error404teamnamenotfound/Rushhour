# Hybrid algorithm 

## Parameters

### minibsf
- looks if 10 steps can be cut to 5
    - "Ten steps are chosen for a shorter runtime on 9x9_5, 9x9_6 and 12x12_7. This because the possibilities on these bords are exponentiely growing and the cars have a lot more options than on the 6x6 bords."

### minibsf_reversed
- looks if 6 steps can be cut to 5
    - "the reversed begins at the end layout and works backwords. To make sure the same move_set is not being used two times another stepsize at least 3 away is chosen. "

### loopremover
- removes all steps between dubble layouts

### bsfhybrid
- Has a extra goal
    - "The normal bsf only stops if the end layout is reached, but the hybrid also stops if the end layout is reached withhout this being the finish."

