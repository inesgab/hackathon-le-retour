from ines import *
from Simon import *
from clemclem import *
import pygame as pg

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




