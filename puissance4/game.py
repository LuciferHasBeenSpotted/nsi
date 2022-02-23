from functions.utils.grille_vide import grille_vide
from functions.utils.clear import clear
from functions.game.afficher import afficher
from functions.game.jouer import jouer
from functions.game.match_nul import match_nul
from functions.game.victoire import victoire

grid = grille_vide()
clear()
p1_pseudo = input('Enter the name of the first player: ')
p2_pseudo = input('Enter the name of the second player: ')

while not(match_nul(grid)):
    afficher(grid)
    p1_choice = int(input(f'{p1_pseudo} choose a column: '))
    grid = jouer(grid, 1, p1_choice)
    afficher(grid)
    if victoire(grid, 1):
        print(f'{p1_pseudo} won the game !: ')
        break
    p2_choice = int(input(f'{p2_pseudo} choose a column: '))
    grid = jouer(grid, 2, p2_choice)
    afficher(grid)
    if victoire(grid, 2):
        print(f'{p2_pseudo} won the game ! ')
        break

print("Developped by 『🌸』 嵐 Lucifer リーダー『🍁』")
