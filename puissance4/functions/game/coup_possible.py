def coup_possible(grid, column):
    '''
    Check if a movement is possible
    Args: grid [grid] (Array of Array of int) & column [column] (int)
    Out: movement possible ? (bool)
    '''
    for line in grid:
        if line[column - 1] == 0:
            return True
    return False
