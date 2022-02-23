from functions.game.horiz import horiz
from functions.game.vert import vert
from functions.game.diag import diag

def victoire(grid: list, player: int):
    '''
    Check on whole grid if a given player won
    Args: grid [grid] (Array of array of int) & player [player] (int)
    Out: Player won ? (bool)
    '''
    for line in range(6):
        for column in range(4):
            if horiz(grid, player, line, column):
                return True
    for column in range(7):
        for line in range(3):
            if vert(grid, player, line, column):
                return True
    for column in range(7):
        for line in range(3):
            if diag(grid, player, line, column):
                return True
