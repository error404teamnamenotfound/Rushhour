import random

no_move = []

def random_move(moves_list):
    global no_move

    # return random move from moves_list

    choice = random.choice(moves_list)

    if choice == no_move:
        
        moves_list.remove(choice)
      
        choice = random.choice(moves_list)

        if choice[1] < 0:
            no_move = [choice[0], 1]
    
        else:
            no_move = [choice[0], -1]

        return choice

    if choice[1] < 0:
        no_move = [choice[0], 1]
    
    else:
        no_move = [choice[0], -1]
    
    return choice
    
