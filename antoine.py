from ines import *
from Simon import *
from clemclem import *
import pygame as pg
import random as rd

LONGUEUR = 700
LARGEUR = 500
FD = 20

CLASSES = {
    "#" : Couloir,
    "|" : Mur,
    "-" : Mur,
    "@" : Perso,
    "+" : Porte,
    " " : Vide,
    "." : Sol,
    "=" : Escalier,
    "G" : Gold,
    "P" : Potion
}

def generation_objet(etage):
    position_potion = ()
    position_gold = ()
    m, n = len(etage), len(etage[0])
    while position_potion == () :
        a, b= rd.randint(0, n-1), rd.randint(0, m-1)
        if type(etage[b][a]) is Sol :
            position_potion = (a, b)
    while position_gold == () :
        a, b = rd.randint(0,n-1), rd.randint(0,m-1)
        if type(etage[b][a]) is Sol :
            position_gold = (a, b)
    return position_gold, position_potion

def trouver_voisins(x, y):
    voisins = []
    for i in range(-2,3):
        for j in range(-2,3):
            voisins.append((x+i, y+j))
    return voisins

def convert_text2lab(fichier: str) -> list:
    etage = []
    collectables = {}
    with open(fichier, 'r') as f:
        for indice_ligne, ligne in enumerate(f):
            ligne_propre = ligne.replace('\n', '')
            ligne_objet = []
            for indice_colonne, char in enumerate(ligne_propre):
                ligne_objet.append(CLASSES[char](indice_colonne, indice_ligne))
                if char == '@' :
                    heros = CLASSES[char](indice_colonne, indice_ligne)
                    ligne_objet.pop()
                    ligne_objet.append(Sol(indice_colonne, indice_ligne))
                if CLASSES[char](indice_colonne, indice_ligne).gettable:
                    collectables[(indice_colonne, indice_ligne)] = CLASSES[char](indice_colonne, indice_ligne)
                    ligne_objet.pop()
                    ligne_objet.append(Sol(indice_colonne, indice_ligne))
            etage.append(ligne_objet)
    return etage, heros, collectables

etage, heros, collectables = convert_text2lab('premier_etage.txt')
visible = set([etage[x][y] for x, y in trouver_voisins(heros.x, heros.y)])
position_gold, position_potion = generation_objet(etage)
collectables_simon = {position_gold : Gold(position_gold[0], position_gold[1]), position_potion : Potion(position_potion[0], position_potion[1])}

pg.init()
screen = pg.display.set_mode((LONGUEUR, LARGEUR))
clock = pg.time.Clock()

running = True

while running:

    clock.tick(10)

    rect = pg.Rect(0, 0, LONGUEUR, LARGEUR)
    pg.draw.rect(screen, WHITE, rect)

    '''for ligne in etage:
        for objet in ligne:
            if not objet.move:
                rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
                pg.draw.rect(screen, objet.color, rect)'''
    
    for objet in visible:
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)

    
    '''for position, objet in collectables.items():
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)

    for position, objet in collectables_simon.items():
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)'''

    rect_heros = pg.Rect(FD*heros.x, FD*heros.y, FD, FD)
    pg.draw.rect(screen, heros.color, rect_heros)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                heros.change_position(HAUT)
                if not etage[heros.y][heros.x].through:
                    heros.change_position(BAS)
            elif event.key == pg.K_s:
                heros.change_position(BAS)
                if not etage[heros.y][heros.x].through:
                    heros.change_position(HAUT)
            elif event.key == pg.K_q:
                heros.change_position(GAUCHE)
                if not etage[heros.y][heros.x].through:
                    heros.change_position(DROITE)
            elif event.key == pg.K_d:
                heros.change_position(DROITE)
                if not etage[heros.y][heros.x].through:
                    heros.change_position(GAUCHE)

    for neighboor in trouver_voisins(heros.x, heros.y):
        visible.add(etage[neighboor[0]][neighboor[1]])
        if neighboor in collectables_simon:
            visible.add(collectables_simon[neighboor])
                    

    pg.display.update()

pg.quit()