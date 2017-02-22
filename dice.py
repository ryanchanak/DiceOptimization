from random import randint


def dice_roll(n):
    '''Returns a value for an 'n' sided-die.'''
    roll = randint(1, n)
    return roll
