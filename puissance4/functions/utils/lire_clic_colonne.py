from pygame import time, quit, mouse
from pygame import event as events
from pygame.locals import QUIT, MOUSEBUTTONDOWN

box_size = 80

def lire_clic_colonne():
    """
    Wait an user's clic on an column
    Out: the clicked column (int)
    """
    while True:
        time.Clock().tick(30)
        for event in events.get():
            if event.type == QUIT:
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = mouse.get_pos()
                return x // box_size
