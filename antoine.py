from ines import *
from Simon import *
from clemclem import *
import pygame as pg
import random as rd

LONGUEUR = 700
LARGEUR = 500
FD = 20

IMGPOTION = pg.image.load('IMAGES/potion.png')

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
    for i in range(-1,2):
        for j in range(-1,2):
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

etage, heros, collectables = convert_text2lab('deux_etage.txt')
visible = set([etage[x][y] for x, y in trouver_voisins(heros.x, heros.y)])

position_gold, position_potion = generation_objet(etage)
invent = Inventaire()
piece = Gold(position_gold[0], position_gold[1])
panoramix = Potion(position_potion[0], position_potion[1])
collectables_simon = {position_gold : piece, position_potion : panoramix}
collectables_visibles = {}
for neighboor in trouver_voisins(heros.x, heros.y):
    if neighboor in collectables_simon:
        collectables_visibles[neighboor] = collectables_simon[neighboor]

pg.init()
screen = pg.display.set_mode((LONGUEUR, LARGEUR))
clock = pg.time.Clock()

running = True

while running:

    clock.tick(10)

    rect = pg.Rect(0, 0, LONGUEUR, LARGEUR)
    pg.draw.rect(screen, BLACK, rect)

    '''for ligne in etage:
        for objet in ligne:
            if not objet.move:
                rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
                pg.draw.rect(screen, objet.color, rect)'''
    
    for objet in visible:
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)

    for objet in collectables_visibles.values():
        if type(objet) is Potion:
            screen.blit(IMGPOTION, (position_potion[0]*FD, position_potion[1]*FD))
        else:
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
        visible.add(etage[neighboor[1]][neighboor[0]])
        if neighboor in collectables_simon:
            collectables_visibles[neighboor] = collectables_simon[neighboor]
    
    if (heros.x, heros.y) == position_potion : 
        invent.get_potion()
        collectables_visibles.pop(position_potion)
        collectables_simon.pop(position_potion)
        position_potion = None

    if (heros.x, heros.y) == position_gold : 
        heros.get_gold(piece)
        collectables_visibles.pop(position_gold)
        collectables_simon.pop(position_gold)
        position_gold = None

    pg.display.update()

pg.quit()