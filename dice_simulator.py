from dice import dice_roll


def dice_simulator(n, j):
    '''Given n number of rolls on j sided dice, 
       return dice rolls
       n numbers of times.'''
    dice_rolls = []
    for i in range(n):
        dice_rolls.append(dice_roll(j))
    return dice_rolls

