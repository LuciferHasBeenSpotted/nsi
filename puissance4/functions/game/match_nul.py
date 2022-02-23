def match_nul(grid: list):
    '''
    Check on the whole grid if there are movements
    Arg: grid [grid] (Array of array of int)
    Out: Are there movements ? (bool)
    '''
    return False if 0 in grid[len(grid) - 1] else True
