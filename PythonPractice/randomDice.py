import random

def roll_die():
    '''roll_die() -> int
    requires the random module
    returns 1,2,3,4,5,6 at random
    '''
    return random.randrange(1, 7)

def take_turn(player):
    '''take_turn(player) -> void
    Takes a turn for the active player.
    player: str
    '''
    input(player + ", press enter to roll.")
    roll = roll_die()
    print(player + " rolled a " + str(roll))
    if roll == 6: 
        print(player + " wins!")
        return True
    return False

someone_won = False
while not someone_won:
    for player in ["Player 1", "Player 2"]:
        someone_won = take_turn(player)
        if someone_won:
            break
