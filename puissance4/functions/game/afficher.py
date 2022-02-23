from functions.utils.clear import clear

def afficher(grid: list):
    '''
    Process and print an given grid
    Arg: Grid (Array of Array of int)
    Out: Processed grid (Array of Array of int)
    '''
    clear()
    new_grid = []
    for line in grid:
        new_line = []
        for item in line:
            if item == 0:
                new_line.append('.')
            elif item == 1:
                new_line.append('O')
            else:
                new_line.append('X')
        new_grid.append(new_line)
    new_grid.reverse()
    for ligne in new_grid:
        print(f'|{"|".join(ligne)}|')
    return new_grid
