from pygame import draw, display

box_size = 80

def afficher_dans_fenetre(window, grid):
    """
    Display the game's grid in the given window, player one in red and player two in blue
    Args: window [window] (pygame window) & grid [grid] (array of array of int)
    Out: Edit the pygame's window
    """
    for line in range(6):
        for column in range(7):
            if grid[line][column] != 0:
                if grid[line][column] == 1:
                    color = (255, 0, 0)
                else:
                    color = (0, 0, 255)
                draw.circle(window, color, (int((column+0.5)*box_size), int((6-line-0.5)*box_size)), int(0.4*box_size))
    display.update()
