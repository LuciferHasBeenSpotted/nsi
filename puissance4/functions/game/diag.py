def diag(grid: list, player: int, l: int, c: int):
    '''
    Determine if the given player wins with an diagonal string of four tokens from a line and column gived
    Args: grid [grid] (Array of Array of int) & player [player] (int) & line to start [l] (int) & column to start [c] (int)
    Out: Gived player wins ? (bool)
    '''
    change = False
    if c in [0, 1, 2]:
        for i in range(4):
            if grid[l + i][c + i] != player:
                return False
    if c in [4, 5, 6]:
        for i in range(4):
            if grid[l + i][c - i] != player:
                return False
    if c == 3:
        for i in range(4):
            if grid[l + i][c + i] != player:
                change = True
            if change:
                for i in range(4):
                    if grid[l + i][c - i] != player:
                        return False
    return True
