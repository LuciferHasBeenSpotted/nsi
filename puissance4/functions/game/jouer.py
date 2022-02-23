from functions.game.coup_possible import coup_possible

def jouer(grid: list, player: int, column: int):
    '''
    Add the token of a given player in the column of a grid both given
    Args: grid [grid] (Array of Array of int) & player [player] (int) & column [column] (int)
    Out: grid with the new token (Array of Array of Int)
    '''
    new_grid = []
    token = (1, 2)[player == 2]
    change = True
    for line in grid:
        new_line = []
        for item_pos in range(len(line)):
            if item_pos == (column - 1) and change == True and coup_possible(grid, column) and line[item_pos] == 0:
                new_line.append(token)
                change = False
            else:
                new_line.append(line[item_pos])
        new_grid.append(new_line)
    return new_grid
