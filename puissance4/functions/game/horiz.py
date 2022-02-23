def horiz(grid: list, player: int, l: int, c: int):
    '''
    Determine if the given player wins with an horizontal string of four tokens from a line and column gived
    Args: grid [grid] (Array of Array of int) & player [player] (int) & line to start [l] (int) & column to start [c] (int)
    Out: Gived player wins ? (bool)
    '''
    for column in range(4):
        if grid[l][c + column] != player:
            return False
    return True
