import pygame
from functions.utils.grille_vide import grille_vide
from functions.game.jouer import jouer
from functions.game.match_nul import match_nul
from functions.game.victoire import victoire
from functions.utils.afficher_dans_fenetre import afficher_dans_fenetre
from functions.utils.lire_clic_colonne import lire_clic_colonne

taille_case = 80
pygame.init()
fenetre = pygame.display.set_mode((7*taille_case, 6*taille_case))
fenetre.fill((255, 255, 255))
for l in range(1, 6):
    pygame.draw.line(fenetre, (0, 0, 0), (0, l*taille_case), (7*taille_case, l*taille_case))
for c in range(1, 7):
    pygame.draw.line(fenetre, (0, 0, 0), (c*taille_case, 0), (c*taille_case, 6*taille_case))
pygame.display.flip()

grid = grille_vide()
while not(match_nul(grid)):
    grid = jouer(grid, 1, lire_clic_colonne() + 1)
    afficher_dans_fenetre(fenetre, grid)
    if victoire(grid, 1):
        break
    grid = jouer(grid, 2, lire_clic_colonne() + 1)
    afficher_dans_fenetre(fenetre, grid)
    if victoire(grid, 2):
        break    

pygame.quit()
