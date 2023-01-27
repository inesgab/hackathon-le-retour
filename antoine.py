from ines import *
from Simon import *
from clemclem import *
import pygame as pg

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
    "=" : Escalier
}

def convert_text2lab(fichier: str) -> list:
    etage = []
    with open(fichier, 'r') as f:
        for indice_ligne, ligne in enumerate(f):
            ligne_propre = ligne.replace('\n', '')
            ligne_objet = []
            for indice_colonne, char in enumerate(ligne_propre):
                ligne_objet.append(CLASSES[char](indice_colonne, indice_ligne))
            etage.append(ligne_objet)
    return etage

etage = convert_text2lab('premier_etage.txt')

pg.init()
screen = pg.display.set_mode((LONGUEUR, LARGEUR))
clock = pg.time.Clock()

running = True

while running:

    clock.tick(10)

    rect = pg.Rect(0, 0, LONGUEUR, LARGEUR)
    pg.draw.rect(screen, (255, 255, 255), rect)

    for ligne in etage:
        for objet in ligne:
            rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
            pg.draw.rect(screen, objet.color, rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()